class ChessBoard:
    rows = 0
    cols = 0
    size = 0
    board = []
    chess_pieces = []

    empty_placement_char = ""
    threatened_placement_char = "T"

    def __init__(self, rows, cols):
        self.rows = int(rows)
        self.cols = int(cols)
        self.size = rows * cols
        self.board = [[self.empty_placement_char] * cols for _ in range(rows)]

    def add_chess_piece(self, chess_piece):
        self.chess_pieces.append(chess_piece)

    def get_layout_for_piece(self, piece):
        """"""
        for x in range(self.rows):
            for y in range(self.cols):
                res = piece.set_area(x, y)
                if res:
                    break

    def get_layout(self):
        for i in self.chess_pieces:
            self.get_layout_for_piece(i)
