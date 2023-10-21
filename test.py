import pytest
from game_controller import GameController
def test_game_score():
    gameController = GameController()
    player_1 = "max"
    player_2 = "kito"
    gameController.player_1 = player_1
    gameController.player_2 = player_2
    assert gameController.get_player_score(player_1) == 0
    assert gameController.get_player_score(player_2) == 0