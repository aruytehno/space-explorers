import random

def generate_civilization():
    tech_level = random.randint(1, 10)
    aggressiveness = random.randint(1, 10)
    friendliness = random.randint(1, 10)
    name = f"Civ-{random.randint(100, 999)}"
    return {
        "name": name,
        "tech_level": tech_level,
        "aggressiveness": aggressiveness,
        "friendliness": friendliness,
    }
