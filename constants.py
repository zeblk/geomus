# Constants for ecosystem simulation

ICON_EMPTY = '⬜'

PLANT_ICONS = {
    'Grass': '🌱',
    'Shrub': '🌿',
    'Tree': '🌳'
}

ANIMAL_ICONS = {
    'Rabbit': '🐇',
    'Deer': '🦌',
    'Wolf': '🐺'
}

# Energy units an animal can store before starving
ANIMAL_INITIAL_ENERGY = {
    'Rabbit': 3,
    'Deer': 4,
    'Wolf': 6,
}

# Probability of reproduction after eating
ANIMAL_REPRODUCE_PROB = {
    'Rabbit': 0.3,
    'Deer': 0.2,
    'Wolf': 0.1,
}

# Initial distribution probabilities (should sum to <= 1.0)
INITIAL_DISTRIBUTION = {
    'Grass': 0.3,
    'Shrub': 0.15,
    'Tree': 0.1,
    'Rabbit': 0.2,
    'Deer': 0.15,
    'Wolf': 0.05
}

PLANT_SPREAD_PROB = {
    'Grass': 0.05,
    'Shrub': 0.02,
    'Tree': 0.01
}
