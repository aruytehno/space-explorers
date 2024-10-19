import pygame
from star_system import StarSystem
from ship import Ship
from civilization import generate_civilization
from game_data import game_state

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intergalactic Odyssey")
clock = pygame.time.Clock()

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 30)

# Генерация звёздной системы
star_system = StarSystem(WIDTH, HEIGHT)

# Список кораблей
ships = [Ship() for _ in range(3)]

# Генерация цивилизаций
civilizations = [generate_civilization() for _ in range(5)]

# Переменная для состояния всплывающего окна
popup_message = ""
popup_active = False


def draw_interface():
    """Отображение панели ресурсов в верхней части экрана."""
    pygame.draw.rect(screen, GRAY, pygame.Rect(0, 0, WIDTH, 50))  # Серый фон для панели
    energy_text = font.render(f"Energy: {game_state['resources']['energy']}", True, WHITE)
    materials_text = font.render(f"Materials: {game_state['resources']['materials']}", True, WHITE)

    screen.blit(energy_text, (10, 10))  # Отображаем текст энергии
    screen.blit(materials_text, (200, 10))  # Отображаем текст материалов


def draw_civilizations():
    """Отображение информации о цивилизациях."""
    for i, civ in enumerate(civilizations):
        civ_text = font.render(
            f"Civ {i + 1}: Tech {civ['tech_level']}, Aggression {civ['aggressiveness']}, Friendliness {civ['friendliness']}",
            True, WHITE)
        screen.blit(civ_text, (10, 60 + i * 30))


def draw_buttons():
    """Отображение кнопок для управления экспедициями."""
    expedition_button = pygame.Rect(10, 500, 120, 40)
    pygame.draw.rect(screen, GREEN, expedition_button)
    screen.blit(font.render("Send Expedition", True, WHITE), (15, 510))

    # Добавление кнопки для закрытия всплывающего окна
    if popup_active:
        close_button = pygame.Rect(650, 500, 120, 40)
        pygame.draw.rect(screen, RED, close_button)
        screen.blit(font.render("Close Popup", True, WHITE), (655, 510))

    return expedition_button, close_button if popup_active else None


def handle_button_click(pos):
    """Обработка нажатий на кнопки."""
    global popup_active, popup_message
    expedition_button, close_button = draw_buttons()

    if expedition_button.collidepoint(pos) and game_state['resources']['energy'] > 0:
        # Отправляем экспедицию
        game_state['resources']['energy'] -= 100  # Уменьшаем энергию
        popup_message = "Expedition Sent!"
        popup_active = True
    elif popup_active and close_button and close_button.collidepoint(pos):
        # Закрываем всплывающее окно
        popup_active = False


def draw_popup():
    """Отображение всплывающего окна."""
    if popup_active:
        popup_rect = pygame.Rect(200, 200, 400, 200)
        pygame.draw.rect(screen, (50, 50, 50), popup_rect)
        pygame.draw.rect(screen, WHITE, popup_rect, 2)  # Обводка
        popup_text = font.render(popup_message, True, WHITE)
        screen.blit(popup_text, (220, 250))


# Главный игровой цикл
running = True
while running:
    screen.fill(BLACK)  # Фон - черный

    star_system.draw(screen)  # Отрисовка звёздной системы

    # Отрисовка кораблей
    for ship in ships:
        ship.move()  # Движение кораблей
        ship.draw(screen)

    # Отображаем интерфейс
    draw_interface()

    # Отображаем информацию о цивилизациях
    draw_civilizations()

    # Отображаем кнопки
    draw_buttons()

    # Отображаем всплывающее окно
    draw_popup()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_click(event.pos)  # Обработка нажатий на кнопки

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
