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


def test_single_case_layout_3_x_3():
    chess_board = ChessBoard(3, 3)

    expected_results = [["", "R", ""], ["", "", ""], ["K", "", "K"]]
    chess_board.add_chess_piece(Rook(chess_board))
    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(King(chess_board))

    chess_board.calculate_layout(chess_board.chess_pieces, chess_board.cells)

    layout = chess_board.layouts[0]

    assert layout == expected_results


def test_example_all_layouts_3_x_3():
    chess_board = ChessBoard(3, 3)

    expected_results = [
        [["K", "", "K"], ["", "", ""], ["", "R", ""]],
        [["K", "", ""], ["", "", "R"], ["K", "", ""]],
        [["", "", "K"], ["R", "", ""], ["", "", "K"]],
        [["", "R", ""], ["", "", ""], ["K", "", "K"]],
    ]
    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(King(chess_board))
    chess_board.add_chess_piece(Rook(chess_board))

    layouts = chess_board.get_results()

    assert layouts[0] == expected_results[0]
    assert layouts[1] == expected_results[2]
    assert layouts[2] == expected_results[1]
    assert layouts[3] == expected_results[3]


def test_example_layout_4_x_4():
    chess_board = ChessBoard(4, 4)

    expected_results = [
        [["", "N", "", "N"], ["", "", "R", ""], ["", "N", "", "N"], ["R", "", "", ""]],
        [["", "N", "", "N"], ["R", "", "", ""], ["", "N", "", "N"], ["", "", "R", ""]],
        [["R", "", "", ""], ["", "N", "", "N"], ["", "", "R", ""], ["", "N", "", "N"]],
        [["", "", "R", ""], ["", "N", "", "N"], ["R", "", "", ""], ["", "N", "", "N"]],
        [["", "R", "", ""], ["N", "", "N", ""], ["", "", "", "R"], ["N", "", "N", ""]],
        [["", "", "", "R"], ["N", "", "N", ""], ["", "R", "", ""], ["N", "", "N", ""]],
        [["N", "", "N", ""], ["", "", "", "R"], ["N", "", "N", ""], ["", "R", "", ""]],
        [["N", "", "N", ""], ["", "R", "", ""], ["N", "", "N", ""], ["", "", "", "R"]],
    ]

    chess_board.add_chess_piece(Rook(chess_board))
    chess_board.add_chess_piece(Rook(chess_board))
    chess_board.add_chess_piece(Knight(chess_board))
    chess_board.add_chess_piece(Knight(chess_board))
    chess_board.add_chess_piece(Knight(chess_board))
    chess_board.add_chess_piece(Knight(chess_board))

    layouts = chess_board.get_results()

    assert layouts[0] == expected_results[2]
    assert layouts[1] == expected_results[5]
    assert layouts[2] == expected_results[4]
    assert layouts[3] == expected_results[6]
    assert layouts[4] == expected_results[3]
    assert layouts[5] == expected_results[7]
    assert layouts[6] == expected_results[0]
    assert layouts[7] == expected_results[1]
