import os
from game_board import Board
os.system("clear")

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
        self.player_1 = input("Please enter your name: ")
        os.system("clear")
        choice = int(input(f"""        Greetings """ + (self.player_1) + """, let the games begin... \n\n To continue, choose from the following game modes:\n
              Player vs Player (1) \n
              Player vs Uncle (2) \n
              Player vs Chucky (3) \n\n""").strip())
        if choice == 1:
            self.mode = 'PVP'
            os.system("clear")
            self.player_2 = input("Please enter player 2's name: ")
            return self.start_game()
        elif choice == 2:
            pass

    def rematch(self):
        self.board.restart_board()
        self.refresh_gamescreen()


    def refresh_gamescreen(self):
        os.system("clear")
        self.print_title()
        self.board.gameboard()
    

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
        self.refresh_gamescreen()
        marker = "X" if current_player == self.player_1  else "O"
        placement = int(input(f"\n {current_player} it's your turn, please choose 1-9: ")) - 1
        self.board.update_boxes(placement, marker)
        current_player_wins = self.board.win_game(marker)
        if current_player_wins:
            self.game_wins.append(current_player)

        

        return current_player_wins

        # do the turn
        # dop the check
        # interpolate current player
        # use variable current_player 
        
    def on_player_win(self, winning_player): 
        self.refresh_gamescreen()
        print(f"{winning_player} wins!\n")
        return input("Would you like to play again? (Y/N): ")

    def pvp(self):
        while True: 
            player_1_wins = self.initiate_and_validate_player_turn(self.player_1)

            if player_1_wins: 
                rematch =  self.on_player_win(self.player_1)
                if rematch == "y":
                    self.rematch()
                    continue
                else:
                    break
  
            player_2_wins =  self.initiate_and_validate_player_turn(self.player_2)

            if player_2_wins: 
                rematch =  self.on_player_win(self.player_2)
                if rematch == "y":
                    self.rematch()
                    continue
                else:
                    break

           