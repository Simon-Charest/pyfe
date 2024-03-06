from cv2 import destroyAllWindows
from numpy import ndarray
from pyfe.animate_board import animate_board
from pyfe.constant import *
from pyfe.initialize_board import initialize_board


def main() -> None:
    # Initialize game
    board: ndarray = initialize_board(SIZE, DENSITY)

    # Run game loop
    animate_board(board)

    # Quit game
    destroyAllWindows()
