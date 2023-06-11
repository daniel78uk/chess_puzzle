from chess.chess_piece import ChessPiece


class Knight(ChessPiece):
    symbol = "N"

    def __init__(self, board):
        self.chessboard = board

    def can_be_placed(self, row, col):
        """This function checks if a piece can be placed

        Args:
            row (int): row
            col (int): col

        Returns:
            bool: if piece can be placed
        """
        available = False

        if (
            col < 0
            or (col > self.chessboard.cols - 1)
            or row < 0
            or (row > self.chessboard.rows - 1)
        ):
            return False

        if (
            not self.disturbs_space(row + 2, col + 1)
            or not self.disturbs_space(row + 2, col - 1)
            or not self.disturbs_space(row - 2, col + 1)
            or not self.disturbs_space(row - 2, col - 1)
            or not self.disturbs_space(row + 1, col + 2)
            or not self.disturbs_space(row - 1, col + 2)
            or not self.disturbs_space(row + 1, col - 2)
            or not self.disturbs_space(row - 1, col - 2)
        ):
            available = True

        return available

    def mark_threatened_cells(self):
        """This function marks cells as threatened so that other piaces cannot be placed"""
        if self.placement_exist(self.row + 2, self.col + 1):
            self.chessboard.board[self.row + 2][
                self.col + 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 2, self.col - 1):
            self.chessboard.board[self.row + 2][
                self.col - 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 2, self.col + 1):
            self.chessboard.board[self.row - 2][
                self.col + 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 2, self.col - 1):
            self.chessboard.board[self.row - 2][
                self.col - 1
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 1, self.col + 2):
            self.chessboard.board[self.row + 1][
                self.col + 2
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 1, self.col + 2):
            self.chessboard.board[self.row - 1][
                self.col + 2
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row + 1, self.col - 2):
            self.chessboard.board[self.row + 1][
                self.col - 2
            ] = self.chessboard.threatened_placement_char

        if self.placement_exist(self.row - 1, self.col - 2):
            self.chessboard.board[self.row - 1][
                self.col - 2
            ] = self.chessboard.threatened_placement_char
