import time
import random
import os
class Bot:
    def __init__(self, parent):
        self.parent = parent
        self.player_1 = player_1()

        
    def initiate_and_validate_bot_player(self, current_player):
        is_valid = False
        placement = None
        prompt_count = 0
        while is_valid == False:
            self.parent.refresh_gamescreen()
            if prompt_count == 1:
                print(f"C'mon {current_player}, wrong move")
            elif prompt_count == 2:
                print(f"C'mon {current_player}, two in a row? Get it together")
            elif prompt_count == 3:
                print(f"OK {current_player}, Last chance or you're opponent gets another crack")
            elif prompt_count >= 4:
                countdown = 0
                while countdown < 4:
                    os.system("clear")
                    print(f"You had three chances, you're sleeping on me!{'.' * countdown}")
                    time.sleep(.5)
                    countdown += 1
                return
            
            marker = "X" if current_player == self.player_1  else "O"
            placement = input(f"\n {current_player} it's your turn, please choose 1-9: ")
            is_valid = placement.isdigit() and (int(placement) >= 1 and int(placement) <= 9) and self.board.box[int(placement) - 1] == " "
            prompt_count += 1
           

        self.parent.board.update_boxes(int(placement) - 1, marker)
        current_player_wins = self.board.win_game(marker)
        if current_player_wins:
            self.game_wins.append(current_player)

        return current_player_wins



    