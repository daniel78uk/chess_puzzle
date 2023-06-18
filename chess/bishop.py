from chess.chess_piece import ChessPiece


class Bishop(ChessPiece):
    symbol = "B"

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
        max_dimension = max(self.chessboard.rows, self.chessboard.cols)

        movements.append([row, col])

        for x in range(max_dimension):
            if not self.is_out_of_bounds(row + x, col + x):
                movements.append([row + x, col + x])

            if not self.is_out_of_bounds(row + x, col - x):
                movements.append([row + x, col - x])

            if not self.is_out_of_bounds(row - x, col + x):
                movements.append([row - x, col + x])

            if not self.is_out_of_bounds(row - x, col - x):
                movements.append([row - x, col - x])

        return movements

    def mark_threatened_cells(self):
        """
        This function marks cells as threatened so that other piaces cannot be placed
        """

        for c in range(max(self.chessboard.rows, self.chessboard.cols)):
            if self.placement_exist(self.row - c, self.col - c):
                self.chessboard.board[self.row - c][self.col - c] = "T"
            if self.placement_exist(self.row - c, self.col + c):
                self.chessboard.board[self.row - c][self.col + c] = "T"
            if self.placement_exist(self.row + c, self.col - c):
                self.chessboard.board[self.row + c][self.col - c] = "T"
            if self.placement_exist(self.row + c, self.col + c):
                self.chessboard.board[self.row + c][self.col + c] = "T"
