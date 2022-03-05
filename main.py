# Jules Dessors : The Eight Queens Problem


def is_possible(matrix: list[list[int]], ilin: int, icol: int) -> bool:
    """Tells if a queen can be placed at a certain position.

    Args:
        matrix (list[list[int]]): The matrix that represents the board.
        ilin (int): The line index.
        icol (int): The column index.

    Returns:
        bool: Wheter it is possible to play a queen here.
    """
    size = len(matrix)

    # Check the vertical line
    for i in range(size):
        if i != icol and matrix[ilin][i] == 1:
            return False

    # Check the NO/SE diago
    offset = icol - ilin
    for i in range(size - abs(offset)):
        if offset >= 0:
            if matrix[i][i + offset] == 1:
                return False
        else:
            if matrix[i - offset][i] == 1:
                return False

    # Check the NE/SO diago
    offset = icol + ilin
    if offset > size-1:
        offset_abs = (size-1)*2 - offset
    else:
        offset_abs = offset
    for i in range(offset_abs + 1):
        if offset <= size-1:
            if matrix[i][offset - i] == 1:
                return False
        else:
            if matrix[i + size - offset_abs - 1][size - i - 1] == 1:
                return False

    # No queens detected, place avalaible
    return True


def fill_matrix(solutions: list, matrix: list[list[int]], icol: int = 0) -> bool:
    """Add a Queen to the board, then fill the new board.

    Args:
        solutions (list): Contains every matrix that is a solution to the problem.
        matrix (list[list[int]]): The matrix that represents the board.
        icol (int): The column where to add the Queen.

    Returns:
        bool: Whether it was possible to put the queen.
    """
    size = len(matrix)
    for ilin in range(size):
        # Check for each line if there is a possible place for the queen
        if is_possible(matrix, ilin, icol):
            matrix[ilin][icol] = 1
            if icol == size - 1:
                # Last col filled, add this board to the solutions
                solutions.append([line[:] for line in matrix])
            else:
                # Columns not all filled, keep going
                fill_matrix(solutions, matrix, icol+1)
            # Delete the changes to test a new position for this column
            matrix[ilin][icol] = 0


def show_matrix(matrix: list[list[int]]) -> None:
    """Print the matrix.

    Args:
        matrix (list[list[int]]): A squared matrix.
    """
    size = len(matrix)
    print('+' + '-' * (size * 2 - 1) + '+')
    for line in matrix:
        print('|' + ' '.join(map(str, line)).replace("0",
              ".").replace("1", "@") + '|')
    print('+' + '-' * (size * 2 - 1) + '+')


if __name__ == '__main__':
    # Create the matrix
    size = int(input("Entrez la taille du plateau: "))
    matrix = [[0]*size for _ in range(size)]
    solutions = []

    # Fill it recursively
    fill_matrix(solutions, matrix)

    # Print it prettifully
    print("%d solutions trouvées.\nPremière solution:" % len(solutions))
    show_matrix(solutions[0])
