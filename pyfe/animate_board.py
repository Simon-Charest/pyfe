from cv2 import imshow, rectangle, waitKey
from numpy import ndarray, uint8, zeros
from pyfe.constant import *
from pyfe.update_board import update_board


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
