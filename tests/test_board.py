from chess.bishop import Bishop
from chess.board import ChessBoard
from chess.king import King
from chess.knight import Knight
from chess.queen import Queen
from chess.rook import Rook


def test_board_creation():
    chess_board = ChessBoard(3, 3)

    assert chess_board.rows == 3
    assert chess_board.cols == 3
    assert chess_board.size == 9
    assert chess_board.board[0] == ["", "", ""]


def test_example_layout_3_x_3():
    chess_board = ChessBoard(3, 3)

    expected_results = [["K", "", "K"], ["", "", ""], ["", "R", ""]]

    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(Rook(chess_board))

    chess_board.get_layout()

    assert chess_board.board == expected_results
