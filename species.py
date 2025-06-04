from dataclasses import dataclass
from constants import PLANT_ICONS, ANIMAL_ICONS

@dataclass
class Organism:
    name: str
    icon: str
    kind: str  # 'plant' or 'animal'

    def __str__(self):
        return self.icon

class Plant(Organism):
    def __init__(self, name: str):
        super().__init__(name, PLANT_ICONS[name], 'plant')

class Animal(Organism):
    def __init__(self, name: str):
        super().__init__(name, ANIMAL_ICONS[name], 'animal')
