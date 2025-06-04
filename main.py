from time import sleep

from grid import Grid
import constants
import tkinter as tk


def run_simulation_console(
    width: int = 20, height: int = 10, steps: int = 50, delay: float = 0.5
) -> None:
    """Run the simulation in the console using text output."""
    grid = Grid(width, height)
    grid.initialize()
    for _ in range(steps):
        grid.display()
        grid.step()
        sleep(delay)


def run_simulation_gui(
    width: int = 20, height: int = 10, steps: int = 50, delay: int = 500
) -> None:
    """Run the simulation with a simple Tkinter GUI."""
    grid = Grid(width, height)
    grid.initialize()

    root = tk.Tk()
    root.title("Ecosystem Simulation")

    labels = [
        [
            tk.Label(root, text=constants.ICON_EMPTY, font=("Arial", 20))
            for _ in range(width)
        ]
        for _ in range(height)
    ]
    for r in range(height):
        for c in range(width):
            labels[r][c].grid(row=r, column=c)

    def update_display() -> None:
        for r in range(height):
            for c in range(width):
                cell = grid.grid[r][c]
                labels[r][c].config(
                    text=str(cell) if cell else constants.ICON_EMPTY
                )

    step_count = 0

    def step() -> None:
        nonlocal step_count
        if step_count >= steps:
            return
        grid.step()
        update_display()
        step_count += 1
        root.after(delay, step)

    update_display()
    root.after(delay, step)
    root.mainloop()


if __name__ == "__main__":
    # Default to GUI when executed directly
    run_simulation_gui()
