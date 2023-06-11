from chess.bishop import Bishop
from chess.board import ChessBoard


def test_distrurb_place():
    chess_board = ChessBoard(3, 3)
    piece = Bishop(chess_board)

    assert piece.disturbs_space(0, 0) == False


def test_can_be_placed():
    chess_board = ChessBoard(3, 3)
    piece = Bishop(chess_board)

    assert piece.can_be_placed(0, 0) == True
    assert piece.can_be_placed(3, 3) == False


def test_spread_cells_top_left():
    chess_board = ChessBoard(3, 3)
    piece = Bishop(chess_board)

    res = piece.set_area(0, 0)

    assert res == True
    assert chess_board.board[0][0] == piece.symbol
    assert chess_board.board[0][1] == ""
    assert chess_board.board[0][2] == ""
    assert chess_board.board[1][0] == ""
    assert chess_board.board[1][1] == "T"
    assert chess_board.board[1][2] == ""
    assert chess_board.board[2][0] == ""
    assert chess_board.board[2][1] == ""
    assert chess_board.board[2][2] == "T"


def test_spread_cells_middle():
    chess_board = ChessBoard(3, 3)
    piece = Bishop(chess_board)

    res = piece.set_area(1, 1)

    assert res == True
    assert chess_board.board[1][1] == piece.symbol
    assert chess_board.board[0][0] == "T"
    assert chess_board.board[0][1] == ""
    assert chess_board.board[0][2] == "T"
    assert chess_board.board[1][0] == ""
    assert chess_board.board[1][2] == ""
    assert chess_board.board[2][0] == "T"
    assert chess_board.board[2][1] == ""
    assert chess_board.board[2][2] == "T"
