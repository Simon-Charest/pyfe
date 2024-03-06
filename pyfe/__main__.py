from cv2 import destroyAllWindows
from numpy import ndarray
from animate_board import animate_board
from constant import *
from initialize_board import initialize_board


def main() -> None:
    # Initialize game
    board: ndarray = initialize_board(SIZE, DENSITY)

    # Run game loop
    animate_board(board)

    # Quit game
    destroyAllWindows()


if __name__ == "__main__":
    main()
