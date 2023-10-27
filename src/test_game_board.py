from game_board import Board
from game_controller import GameController
import pytest

gameBoard = Board()
gameController = GameController()

def test_update_boxes():
    player_1 = "X"
    player_2 = "O"
    gameController.player_1 = player_1
    gameController.player_2 = player_2
    gameBoard.update_boxes(0, player_1)
    assert gameBoard.box == ["X", " ", " ", " ", " ", " ", " ", " ", " "]
    gameBoard.update_boxes(1, player_2)
    assert gameBoard.box == ["X", "O", " ", " ", " ", " ", " ", " ", " "]

def test_tie_game():
    gameBoard.box = ["X", "O", "X", "O", "O", "X", "X", "X", "O"]
    assert gameBoard.tie_game() == True
    gameBoard.box = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    assert gameBoard.tie_game() == False

def test_win_game():
    player_1 = "X"
    gameController.player_1 = player_1
    gameBoard.box = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
    assert gameBoard.win_game(player_1) == True
    gameBoard.box = ["X", "O", "X", "O", "O", "X", "X", "X", "O"]
    assert gameBoard.win_game(player_1) == False

