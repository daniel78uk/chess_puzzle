from chess.chess_piece import ChessPiece


class King(ChessPiece):
    symbol = "K"

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

        # ensure that this space doesn't threaten an existing piece,
        # if a location is neither empty, nor threatened, then a piece is in that location
        if (
            not self.disturbs_space(row + 1, col + 1)
            or not self.disturbs_space(row - 1, col + 1)
            or not self.disturbs_space(row + 1, col - 1)
            or not self.disturbs_space(row - 1, col - 1)
            or not self.disturbs_space(row, col + 1)
            or not self.disturbs_space(row, col - 1)
            or not self.disturbs_space(row + 1, col)
            or not self.disturbs_space(row - 1, col)
        ):
            available = True

        return available

    def mark_threatened_cells(self):
        """This function marks cells as threatened so that other piaces cannot be placed"""
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
