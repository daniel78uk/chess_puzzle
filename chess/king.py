from chess.chess_piece import ChessPiece


class King(ChessPiece):
    symbol = "K"

    def __init__(self, board):
        ChessPiece.__init__(self, board)

    def get_movements(self, row, col):
        """
        Gets all possible movements for the chess piece

        Args:
            row (int): row
            col (int): col

        Returns:
            arr: list of movements for the chess piece
        """
        movements = []

        movements.append([row, col])

        if not self.is_out_of_bounds(row, col + 1):
            movements.append([row, col + 1])

        if not self.is_out_of_bounds(row, col - 1):
            movements.append([row, col - 1])

        if not self.is_out_of_bounds(row + 1, col):
            movements.append([row + 1, col])

        if not self.is_out_of_bounds(row + 1, col - 1):
            movements.append([row + 1, col - 1])

        if not self.is_out_of_bounds(row + 1, col + 1):
            movements.append([row + 1, col + 1])

        if not self.is_out_of_bounds(row - 1, col):
            movements.append([row - 1, col])

        if not self.is_out_of_bounds(row - 1, col - 1):
            movements.append([row - 1, col - 1])

        if not self.is_out_of_bounds(row - 1, col + 1):
            movements.append([row - 1, col + 1])

        return movements

    def mark_threatened_cells(self):
        """
        This function marks cells as threatened so that other piaces cannot be placed
        """

        if self.placement_exist(self.row, self.col + 1):
            self.chessboard.board[self.row][
                self.col + 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row, self.col - 1):
            self.chessboard.board[self.row][
                self.col - 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 1, self.col):
            self.chessboard.board[self.row + 1][
                self.col
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 1, self.col + 1):
            self.chessboard.board[self.row + 1][
                self.col + 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 1, self.col - 1):
            self.chessboard.board[self.row + 1][
                self.col - 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 1, self.col):
            self.chessboard.board[self.row - 1][
                self.col
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 1, self.col + 1):
            self.chessboard.board[self.row - 1][
                self.col + 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 1, self.col - 1):
            self.chessboard.board[self.row - 1][
                self.col - 1
            ] = self.chessboard.threatened_placement_char
