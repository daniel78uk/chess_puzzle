from chess.bishop import Bishop
from chess.board import ChessBoard
from chess.king import King
from chess.knight import Knight
from chess.queen import Queen
from chess.rook import Rook


def chess_puzzle_solution():
    chess_board = ChessBoard(6, 9)

    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(Queen(chess_board))
    chess_board.add_chess_piece(Bishop(chess_board))
    chess_board.add_chess_piece(Rook(chess_board))
    chess_board.add_chess_piece(Knight(chess_board))

    layouts = chess_board.get_results()

    for layout in layouts:
        print(str(layout))


chess_puzzle_solution()
