from chess.chess_piece import ChessPiece


class Rook(ChessPiece):
    symbol = "R"

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

        for x in range(max(self.chessboard.rows, self.chessboard.cols)):
            if (
                (col - x) < 0
                or ((col + x) > self.chessboard.cols - 1)
                or (row - x) < 0
                or ((row + x) > self.chessboard.rows - 1)
            ):
                break

            if not self.disturbs_space(row, x) or not self.disturbs_space(x, col):
                available = True
                break

        return available

    def mark_threatened_cells(self):
        """This function marks cells as threatened so that other piaces cannot be placed"""

        for k in range(max(self.chessboard.rows, self.chessboard.cols)):
            if self.placement_exist(k, self.col):
                self.chessboard.board[k][self.col] = "T"
            if self.placement_exist(self.row, k):
                self.chessboard.board[self.row][k] = "T"
