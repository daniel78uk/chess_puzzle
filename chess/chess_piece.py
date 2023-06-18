class ChessPiece:
    chessboard = None
    symbol = ""

    allowed_chess_pieces = ["B", "K", "N", "Q", "R"]

    def __init__(self, board):
        self.chessboard = board

    def mark_threatened_cells(self):
        pass

    def get_movements(self, row, col):
        pass

    def is_out_of_bounds(self, row, col):
        """
        Checks if a chesspiece position fall outside the chessboard

        Args:
            row (int): row
            col (int): col

        Returns:
            bool: is inside the chessboard
        """
        if (
            col < 0
            or (col > self.chessboard.cols - 1)
            or row < 0
            or (row > self.chessboard.rows - 1)
        ):
            return True

        return False

    def can_be_placed(self, row, col):
        """
        Checks if a piece can be placed

        Args:
            row (int): row
            col (int): col

        Returns:
            bool: if piece can be placed
        """
        can_be_placed = True

        if self.is_out_of_bounds(row, col):
            return False

        item = self.chessboard.board[row][col]
        is_threatened_placement = item == self.chessboard.threatened_placement_char
        is_chess_piece_placement = item not in self.allowed_chess_pieces

        if is_threatened_placement and is_chess_piece_placement:
            return False

        movements = self.get_movements(row, col)

        if len(movements) == 0:
            return False

        # it does ensure that this space doesn't threaten an existing piece,
        # if a location is neither empty, nor threatened, then a piece is in that location
        for coordinates in movements:
            if self.disturbs_space(coordinates[0], coordinates[1]):
                can_be_placed = False
                break

        return can_be_placed

    def disturbs_space(self, row, col):
        """
        This function checks if a piece can be placed
        checks if row cols are outbounds
        checks if is a threatened spot
        checks if its an empty spot

        Args:
            row (int): row
            col (int): col

        Returns:
            bool: if piece can be placed
        """

        # the first two checks are to make sure the indecolis in-bounds.
        # if indecolout of bounds, just let the caller know
        # if it's neither empty, nor threatened, then it is a piece

        item = self.chessboard.board[row][col]

        is_not_empty_placement = (
            self.chessboard.board[row][col] != self.chessboard.empty_placement_char
        )

        is_threatened_placement = item == self.chessboard.threatened_placement_char

        is_chess_piece_placement = item not in self.allowed_chess_pieces

        disturbs_space = (
            is_not_empty_placement
            and not is_chess_piece_placement
            and not is_threatened_placement
        )

        return disturbs_space

    def placement_exist(self, row, col):
        """
        Check cell to place a threatened one
        The cell needs to be an empty one and not out of the board bounds

        Args:
             row (int): row
             col (int): col

         Returns:
             bool: if piece can be placed
        """

        return not self.is_out_of_bounds(row, col) and (
            self.chessboard.board[row][col] == self.chessboard.empty_placement_char
        )

    def set_area(self, row, col):
        """
        This function puts a piace on the board and runs functions to marks cells

        Args:
            row (int): row
            col (int): col
        """
        res = self.can_be_placed(row, col)

        if res:
            self.row = row
            self.col = col
            self.chessboard.board[row][col] = self.symbol
            self.mark_threatened_cells()

            return True

        return False
