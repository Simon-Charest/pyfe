from numpy import count_nonzero, ndarray


def count_neighbors(board: ndarray, x: int, y: int) -> int:
    """Count the number of live neighbors around a cell."""
    
    neighborhood: ndarray = board[max(0, x - 1):min(x + 2, board.shape[0]), max(0, y - 1):min(y + 2, board.shape[1])]
    
    return int(count_nonzero(neighborhood) - board[x, y])
