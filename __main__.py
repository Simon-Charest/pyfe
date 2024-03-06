from cv2 import destroyAllWindows, imshow, rectangle, waitKey
from numpy import count_nonzero, int32, ndarray, uint8, where, zeros, zeros_like
from numpy.random import choice
from pyfe.constant import *


def main() -> None:
    # Initialize game
    board: ndarray = initialize_board(SIZE, DENSITY)

    # Run game loop
    animate_board(board)

    # Quit game
    destroyAllWindows()


def initialize_board(size: int, density=0.5) -> ndarray:
    """Initialize the board with random cells."""

    return choice([0, 1], size=(size, size), p=[1 - density, density])


def animate_board(board: ndarray):
    """Animate the evolution of the board using OpenCV."""
    
    new_board: ndarray
    size: int = len(board)
    screen_size = CELL_SIZE * size
    display_board: ndarray[uint8]
    i: int
    j: int
    color: tuple[int, int, int]

    # Run game loop
    while True:
        new_board = update_board(board)
        display_board = zeros((screen_size, screen_size, 3), dtype=uint8)

        for i in range(size):
            for j in range(size):
                color = COLOR_WHITE if new_board[i, j] == 1 else COLOR_BLACK
                rectangle(
                    display_board,
                    (j * CELL_SIZE, i * CELL_SIZE),
                    ((j + 1) * CELL_SIZE - 1, (i + 1) * CELL_SIZE - 1),
                    color,
                    -1,
                )

        imshow(TITLE, display_board)
        board = new_board.copy()

        if waitKey(DELAY) & 0xFF in QUIT_KEYS:
            break


def update_board(board: ndarray) -> ndarray:
    """Update the board according to the rules of the Game of Life."""

    i: int
    j: int
    neighbors: int = zeros_like(board, dtype=int32)

    for i in range(len(board)):
        for j in range(len(board)):
            neighbors[i, j] = count_neighbors(board, i, j)

    new_board: ndarray = where((board == 1) & ((neighbors < 2) | (neighbors > 3)), 0, board)
    new_board = where((board == 0) & (neighbors == 3), 1, new_board)

    return new_board


def count_neighbors(board: ndarray, x: int, y: int) -> int:
    """Count the number of live neighbors around a cell."""
    
    neighborhood: ndarray = board[max(0, x - 1):min(x + 2, board.shape[0]), max(0, y - 1):min(y + 2, board.shape[1])]
    
    return int(count_nonzero(neighborhood) - board[x, y])
    

if __name__ == "__main__":
    main()
