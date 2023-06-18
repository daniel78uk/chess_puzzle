def rotate_matrix(matrix):
    """
    Tanspose matrix

    Args:
        matrix (arr): _description_

    Returns:
        arr: transposed matrix
    """
    transposed = []

    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []

    for row in transposed:
        rotated.append(row[::-1])

    return rotated


def unique_matrix_list(matrix_list):
    """
    This returns unique matrix from a list

    Args:
        matrix_list (arr): arr of matrix

    Returns:
        arr: unique martix combinations
    """
    matrix_keys = []
    unique_list = []

    for martix in matrix_list:
        matrix_key = hash(str(martix))

        if matrix_key not in matrix_keys:
            matrix_keys.append(matrix_key)
            unique_list.append(martix)

    return unique_list
