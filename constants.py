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
