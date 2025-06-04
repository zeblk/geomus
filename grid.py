import random
from typing import List, Optional, Tuple

from constants import (
    ICON_EMPTY,
    INITIAL_DISTRIBUTION,
    PLANT_SPREAD_PROB,
)
from species import Plant, Animal, Organism

Position = Tuple[int, int]

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Optional[Organism]]] = [
            [None for _ in range(width)] for _ in range(height)
        ]

    def initialize(self) -> None:
        choices = []
        weights = []
        for name, prob in INITIAL_DISTRIBUTION.items():
            choices.append(name)
            weights.append(prob)
        for r in range(self.height):
            for c in range(self.width):
                organism_name = random.choices(choices + [None], weights + [1 - sum(weights)])[0]
                if organism_name:
                    if organism_name in PLANT_SPREAD_PROB:
                        self.grid[r][c] = Plant(organism_name)
                    else:
                        self.grid[r][c] = Animal(organism_name)

    def neighbors(self, r: int, c: int) -> List[Position]:
        neigh = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.height and 0 <= nc < self.width:
                neigh.append((nr, nc))
        return neigh

    def display(self) -> None:
        for row in self.grid:
            line = ''.join(str(cell) if cell else ICON_EMPTY for cell in row)
            print(line)
        print()

    def step(self) -> None:
        new_grid: List[List[Optional[Organism]]] = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]
        # Process plants first to avoid being immediately eaten after spreading
        for r in range(self.height):
            for c in range(self.width):
                org = self.grid[r][c]
                if isinstance(org, Plant):
                    new_grid[r][c] = org  # plant stays
                    for nr, nc in self.neighbors(r, c):
                        if self.grid[nr][nc] is None and new_grid[nr][nc] is None:
                            # Shade rule: grass/shrub can't grow next to trees
                            if org.name != 'Tree':
                                if any(
                                    isinstance(self.grid[tr][tc], Plant) and self.grid[tr][tc].name == 'Tree'
                                    for tr, tc in self.neighbors(nr, nc)
                                ):
                                    continue
                            if random.random() < PLANT_SPREAD_PROB[org.name]:
                                new_grid[nr][nc] = Plant(org.name)
        # Process animals
        processed = set()
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) in processed:
                    continue
                org = self.grid[r][c]
                if isinstance(org, Animal):
                    destinations = self.neighbors(r, c)
                    random.shuffle(destinations)
                    moved = False
                    # Hunt or graze
                    prey_types = {'Wolf': ['Rabbit', 'Deer']}.get(org.name, ['Grass', 'Shrub', 'Tree'])
                    for nr, nc in destinations:
                        target = self.grid[nr][nc]
                        if target and target.name in prey_types:
                            new_grid[nr][nc] = org
                            processed.add((nr, nc))
                            moved = True
                            break
                    if not moved:
                        # move to empty space
                        for nr, nc in destinations:
                            if self.grid[nr][nc] is None and new_grid[nr][nc] is None:
                                new_grid[nr][nc] = org
                                processed.add((nr, nc))
                                moved = True
                                break
                    if not moved:
                        new_grid[r][c] = org
                        processed.add((r, c))
                elif org and not isinstance(org, Plant):
                    new_grid[r][c] = org
        self.grid = new_grid
