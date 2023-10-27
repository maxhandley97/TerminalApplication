import pytest
from game_controller import GameController
gameController = GameController()

def test_turn_on_game():
    player_1 = "Max"
    gameController.player_1 = "Max"
    assert gameController.player_1 == player_1

def test_game_score():
    player_1 = "Max"
    player_2 = "John"
    gameController.player_1 = player_1
    gameController.player_2 = player_2
    assert gameController.get_player_score(player_1) == 0
    assert gameController.get_player_score(player_2) == 0

    gameController.game_wins = [player_1]
    assert gameController.get_player_score(player_1) == 1
    assert gameController.get_player_score(player_2) == 0

    gameController.game_wins = [player_2, player_2]
    assert gameController.get_player_score(player_1) == 0
    assert gameController.get_player_score(player_2) == 2

def test_validate_player_turn():
    player_1 = "Max"
    player_2 = "John"
    gameController.player_1 = player_1
    gameController.player_2 = player_2
    







