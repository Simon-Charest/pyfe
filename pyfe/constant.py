CELL_SIZE: int = 5  # Size of each cell in pixels
COLOR_BLACK: tuple[int, int, int] = (0, 0, 0)
COLOR_WHITE: tuple[int, int, int] = (255, 255, 255)
DELAY: float = 16  # 16.67 milliseconds of delay between frames is approximately 60 frames per second
DENSITY: float = 0.2  # Initial density of live cells
QUIT_KEYS: list[int] = [27, ord("Q"), ord("q")]  # Escape and Q
SIZE: int = 150  # Size of the board
TITLE: str = "Conway's Game of Life"
