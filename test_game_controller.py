import pytest
from game_controller import GameController
def test_game_score():
    gameController = GameController()
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







