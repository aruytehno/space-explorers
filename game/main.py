import pygame
from star_system import StarSystem
from ship import Ship
from civilization import generate_civilization

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Intergalactic Odyssey")
clock = pygame.time.Clock()

# Генерация звёздной системы
star_system = StarSystem(WIDTH, HEIGHT)

# Список кораблей
ships = [Ship() for _ in range(3)]

# Генерация цивилизаций
civilizations = [generate_civilization() for _ in range(5)]

# Главный игровой цикл
running = True
while running:
    screen.fill((0, 0, 0))  # Фон
    star_system.draw(screen)  # Отрисовка звёздной системы

    # Отрисовка кораблей
    for ship in ships:
        ship.move()  # Движение кораблей
        ship.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
