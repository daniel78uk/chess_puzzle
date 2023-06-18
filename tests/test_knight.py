from chess.board import ChessBoard
from chess.knight import Knight
from chess.rook import Rook


def test_distrurb_place():
    chess_board = ChessBoard(3, 3)
    piece = Knight(chess_board)

    assert piece.disturbs_space(0, 0) == False


def test_can_be_placed():
    chess_board = ChessBoard(3, 3)
    piece = Knight(chess_board)

    assert piece.can_be_placed(0, 0) == True
    assert piece.can_be_placed(3, 3) == False


def test_set_area():
    chess_board = ChessBoard(5, 5)
    first_piece = Knight(chess_board)
    second_piece = Knight(chess_board)
    third_piece = Knight(chess_board)

    assert first_piece.set_area(0, 0) == True
    assert second_piece.set_area(1, 1) == True
    assert third_piece.set_area(1, 2) == False


def test_spread_cells_top_left():
    chess_board = ChessBoard(3, 3)
    piece = Knight(chess_board)

    res = piece.set_area(0, 0)

    assert res == True
    assert chess_board.board[0][0] == piece.symbol
    assert chess_board.board[0][1] == ""
    assert chess_board.board[1][1] == ""
    assert chess_board.board[1][0] == ""
    assert chess_board.board[1][2] == "T"
    assert chess_board.board[2][0] == ""
    assert chess_board.board[2][1] == "T"
    assert chess_board.board[2][2] == ""


def test_spread_cells_middle_4_x_4():
    chess_board = ChessBoard(4, 4)
    first_piece = Knight(chess_board)
    second_piece = Knight(chess_board)
    third_piece = Knight(chess_board)

    res_1 = first_piece.set_area(0, 0)
    res_2 = second_piece.set_area(1, 2)
    res_3 = third_piece.set_area(3, 2)

    assert res_1 == True
    assert chess_board.board[0][0] == first_piece.symbol
    assert chess_board.board[1][2] == "T"
    assert chess_board.board[2][1] == "T"

    assert res_2 == False

    assert res_3 == True
    assert chess_board.board[3][2] == third_piece.symbol
    assert chess_board.board[1][1] == "T"
    assert chess_board.board[1][3] == "T"
    assert chess_board.board[2][0] == "T"


def test_spread_cells_middle_mixed_pieces_4_x_4():
    chess_board = ChessBoard(4, 4)
    first_piece = Rook(chess_board)
    second_piece = Knight(chess_board)
    third_piece = Knight(chess_board)

    res_1 = first_piece.set_area(0, 0)
    res_2 = second_piece.set_area(0, 1)
    res_3 = third_piece.set_area(3, 3)

    assert res_1 == True
    assert chess_board.board[0][0] == first_piece.symbol
    assert chess_board.board[0][1] == "T"
    assert chess_board.board[0][2] == "T"
    assert chess_board.board[0][3] == "T"
    assert chess_board.board[1][0] == "T"
    assert chess_board.board[2][0] == "T"
    assert chess_board.board[3][0] == "T"

    assert res_2 == False

    assert res_3 == True
