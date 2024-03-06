
from numpy import int32, ndarray, where, zeros_like
from count_neighbors import count_neighbors


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
