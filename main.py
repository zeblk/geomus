from time import sleep

from grid import Grid


def run_simulation(width: int = 20, height: int = 10, steps: int = 50, delay: float = 0.5) -> None:
    grid = Grid(width, height)
    grid.initialize()
    for _ in range(steps):
        grid.display()
        grid.step()
        sleep(delay)


if __name__ == "__main__":
    run_simulation()
