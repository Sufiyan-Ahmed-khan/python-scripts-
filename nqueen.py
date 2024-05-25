def is_safe(board, row, col, N):
    """
    A utility function to check if a queen can
    be placed on board[row][col]. Note that this
    function is called when "col" queens are
    already placed in columns from 0 to col -1.
    So we need to check only left side for
    attacking queens.
    """

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N):
    """
    A recursive utility function to solve N
    Queen problem
    """

    # Base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):

        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in
    # this column col then return false
    return False


def solve_n_queens(N):
    """
    The main function to solve N Queen problem
    """
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_board(board)
    return True


def print_board(board):
    """
    A utility function to print solution
    """
    for row in board:
        print(" ".join(map(str, row)))


# Example usage:
n = input("enter your num")
solve_n_queens(n)
