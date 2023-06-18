import copy
from itertools import permutations

import numpy as np

from chess.matrix import rotate_matrix, unique_matrix_list


class ChessBoard:
    rows = 0
    cols = 0
    size = 0
    board = []
    chess_pieces = []
    cells = []

    layouts_keys = []
    layouts = []

    empty_placement_char = ""
    threatened_placement_char = "T"

    def __init__(self, rows=0, cols=0, board=[]):
        self.rows = int(rows)
        self.cols = int(cols)
        self.size = rows * cols
        self.board = (
            board
            if len(board) > 0
            else [[self.empty_placement_char] * cols for _ in range(rows)]
        )
        self.cells = np.array(
            [["%s,%s" % (i, j) for j in range(cols)] for i in range(rows)]
        ).flatten()
        self.chess_pieces = []
        self.layouts = []
        self.layouts_keys = []

    def reset_board(self):
        """
        Clears board

        Returns:
            arr: cleared chessboard for next iteration
        """
        self.board = [[self.empty_placement_char] * self.cols for _ in range(self.rows)]

    def add_chess_piece(self, chess_piece):
        """
        Add chess piece

        Args:
            chess_piece (ChessPiece): Any defined chesspiece
        """
        self.chess_pieces.append(chess_piece)

    def get_cleared_layout(self):
        """
        Returns a clear layout for comparison

        Returns:
            arr: cleared layout
        """
        board_copy = copy.deepcopy(self.board)

        for x in range(self.rows):
            for y in range(self.cols):
                if board_copy[x][y] == self.threatened_placement_char:
                    board_copy[x][y] = self.empty_placement_char

        return board_copy

    def get_layout_for_piece(self, piece, cells):
        """
        Tries to set a value for the current chess piece

        Args:
            piece (ChessPiece): Any defined chesspiece
            cells (arr): arr of cell coordinates

        Returns:
            bool: if all a position has been found for the chess piece
        """
        for cell in cells:
            [row, col] = cell.split(",")

            res = piece.set_area(int(row), int(col))

            if res:
                return True

        return False

    def calculate_layout(self, chess_pieces, cells):
        """
        Main function which iterates over all the cells to find all possible layouts

        Args:
            cells (list, optional): list of cells. Defaults to [].

        Returns:
            arr: list of layouts
        """
        pieces_set = 0
        pieces_num = len(chess_pieces)

        for i in chess_pieces:
            has_piece_been_set = self.get_layout_for_piece(i, cells)

            if has_piece_been_set:
                pieces_set += 1

        if pieces_set == pieces_num:
            layout = self.get_cleared_layout()
            layout_key = hash(str(layout))

            if layout_key not in self.layouts_keys:
                self.layouts_keys.append(layout_key)
                self.layouts.append(layout)
                self.reset_board()

        # if no solution is found by starting from current cell
        # restart positioning of all piaces from next cell
        cells = np.delete(cells, 0)

        self.reset_board()

        if len(cells) > 0:
            self.calculate_layout(chess_pieces, cells)

    def get_all_chess_pieces_permutations(self):
        """
        Get chess pieces permutations

        Returns:
            arr: chess pieces
        """

        all_pieces_permutated = list(permutations(self.chess_pieces))

        return all_pieces_permutated

    def get_results(self):
        """
        Get results for all layouts combinations
        """
        permutated_chess_pieces = self.get_all_chess_pieces_permutations()
        cells = self.cells.copy()

        for chess_pieces in permutated_chess_pieces:
            self.calculate_layout(chess_pieces, cells)

        # rotate solutions
        # this is an assumption that I have taken by looking at the matrix example solutions
        # for the 3x3 and 4x4 boards
        # this should shave off managing the complexity of pieces like the knight which accepts
        # a piece on his side
        # the other option would be getting all layout for the first piece
        # then run those boards for the subsequent pieces

        layouts = []

        for layout in self.layouts:
            layouts.append(layout)
            layouts.append(rotate_matrix(layout))
            layouts.append(rotate_matrix(layout))
            layouts.append(rotate_matrix(layout))

        unique_layouts = unique_matrix_list(layouts)

        return unique_layouts
