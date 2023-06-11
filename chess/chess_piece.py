class ChessPiece:
    chessboard = None
    symbol = ""
    row = -1
    col = -1

    def __init__(self, board):
        self.chessboard = board

    def mark_threatened_cells(self):
        pass

    def can_be_placed(self, row, col):
        pass

    def disturbs_space(self, row, col):
        """This function checks if a piece can be placed
        check if row cols are outbounds
        check if is a threatened spot
        check if its an empty spot

        Args:
            row (int): row
            col (int): col

        Returns:
            bool: if piece can be placed
        """
        # the first two checks are to make sure the indecolis in-bounds. if indecolout of bounds, just let the caller know
        # that it's not threatening things out of bounds. it's not even really a lie, and simplifies several checks.
        # if it's neither empty, nor threatened, then it is a piece

        if row >= self.chessboard.rows or row < 0:
            return True

        if col >= self.chessboard.cols or col < 0:
            return True

        return (
            self.chessboard.board[row][col] != self.chessboard.empty_placement_char
            and self.chessboard.board[row][col]
            != self.chessboard.threatened_placement_char
        )

    def placement_exist(self, row, col):
        return (
            0 <= row < self.chessboard.rows
            and 0 <= col < self.chessboard.cols
            and (
                self.chessboard.board[row][col] == self.chessboard.empty_placement_char
            )
        )

    def set_area(self, row, col):
        """This function puts a piace on the board and runs functions to marks cells

        Args:
            row (int): row
            col (int): col
        """
        if self.can_be_placed(row, col):
            self.row = row
            self.col = col
            self.chessboard.board[row][col] = self.symbol
            self.mark_threatened_cells()

            return True

        return False
