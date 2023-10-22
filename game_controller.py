import os
from game_board import Board
import time

class GameController:
    def __init__(self):
        self.board = Board()
        self.mode = 'PVP'
        self.player_1 = ""
        self.player_2 = ""
        self.game_wins = []
    
    def turn_on_game(self):
        pass
            

    def choose_mode(self):
        if self.player_1 ==  "":
            self.player_1 = input("Please enter your name: ")
            os.system("clear")
        choice = self.get_number(input(f"""        Greetings """ + (self.player_1) + """, let the games begin... \n\n To continue, choose from the following game modes:\n
              Player vs Player (1) \n
              Player vs Drunk Uncle (2) \n
              Player vs Chucky (3) \n\n""").strip())
        if choice == 1:
            self.mode = 'PVP'
            os.system("clear")
            print("You have selected Player Vs Player \n")
            self.player_2 = input("Please enter your challengers name: \n")
            return self.start_game()
        elif choice == 2:
            pass
        else:
            os.system("clear")
            print("     The previous answer was an incorrect choice \n\n")
            self.choose_mode()
            

    def get_number(self, message):
            number = None
            try:
                number = int(message)
            except ValueError:
                print("You need to enter a number")
            return number

    def rematch(self):
        self.board.restart_board()
        self.refresh_gamescreen()


    def refresh_gamescreen(self):
        os.system("clear")
        self.print_title()
        self.board.gameboard()
        if len(self.game_wins) % 2:
            print(f"{self.player_2} you go first")
        else:
            pass
    
    def alternate_player(self):
        if len(self.game_wins) % 2:
            return self.initiate_and_validate_player_turn(self.player_2)
        else:
            pass
            

    def start_game(self): 
        if self.mode == 'PVP':
            return self.pvp()
        

    def get_player_score(self, player):
        return len(list(filter(lambda player_win: player_win == player, self.game_wins)))

    def print_title(self):
        print(f"   {self.mode} \n\nNaughts and Crosses\n")
        if len(self.game_wins) > 0:
            print(f" {self.player_1}: {self.get_player_score(self.player_1)}  VS {self.player_2}: {self.get_player_score(self.player_2)} \n\n")

    def initiate_and_validate_player_turn(self, current_player):
        is_valid = False
        placement = None
        prompt_count = 0
        while is_valid == False:
            self.refresh_gamescreen()
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
           

        self.board.update_boxes(int(placement) - 1, marker)
        current_player_wins = self.board.win_game(marker)
        if current_player_wins:
            self.game_wins.append(current_player)

        return current_player_wins
    
    def on_tie_game(self): 
        self.refresh_gamescreen()
        print ("\nTie game\n")
        return input("Would you like to play again? (Y/N): ").lower()

    def on_player_win(self, winning_player): 
        self.refresh_gamescreen()
        print(f"{winning_player} wins!\n")
        return input("Would you like to play again? (Y/N): ").lower()

    def pvp(self):
        # check for player 1 win
        while True: 
            player_1_wins = self.initiate_and_validate_player_turn(self.player_1)

            if player_1_wins: 
                rematch = self.on_player_win(self.player_1)
                if rematch == "y":
                    self.rematch()
                    self.alternate_player()
                    continue
                else:
                    break

            if self.board.tie_game():
                self.on_tie_game()
                self.rematch()
                break

        #check for player two win
  
            player_2_wins =  self.initiate_and_validate_player_turn(self.player_2)

            if player_2_wins: 
                rematch = self.on_player_win(self.player_2)
                if rematch == "y":
                    self.rematch()
                    self.alternate_player()
                    continue
                else:
                    break

            if self.board.tie_game():
                print ("\nTie game\n")
                break
                


           