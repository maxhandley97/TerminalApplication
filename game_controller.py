import os
from game_board import Board
from bots import Bot
import time
import random
from colort import colorize, ForegroundColor as fc, Style
class GameController:
    def __init__(self):
        self.board = Board()
        # self.drunk_uncle = Bot(self)
        self.player_1 = ""
        self.player_2 = ""
        self.game_wins = []
        self.mode = ""
        self.games_played = 0
        self.versus_bot = False
    
    def turn_on_game(self):
        if self.player_1 ==  "":
            os.system("clear")
            self.player_1 = input("Please enter your name: ")
        return self.choose_mode() 
            

    def choose_mode(self):
        os.system("clear")
        choice = self.get_number(input(f"""        Greetings """ + (self.player_1) + """, let the games begin... \n\n To continue, choose from the following game modes:\n
              Player vs Player (1) \n
              Player vs Drunk Uncle (2) \n
              Player vs Chucky (3) \n\n""").strip())
        if choice == 1:
            os.system("clear")
            print("You have selected Player Vs Player \n")
            self.player_2 = input("Please enter your challengers name: \n")
            self.mode = "Player vs Player"
            self.versus_bot = False
            return self.pvp()
        
        elif choice == 2:
            self.mode = "Player vs Drunk Uncle"
            self.player_2 = "Drunk Uncle"
            self.versus_bot = True
            return self.pvp()
        
        elif choice == 3:
            self.mode = "Player vs Chucky"
            self.player_2 = "Chucky"
            self.versus_bot = True
            return self.pvp()
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
                time.sleep(1)
            return number

    def rematch(self):
        self.board.restart_board()
        self.refresh_gamescreen()
        


    def refresh_gamescreen(self):
        os.system("clear")
        self.print_title()
        self.print_scoreboard()
        self.board.gameboard()
        
    
    def alternate_player(self):
        if len(self.games_played) % 2:
            return self.initiate_and_validate_player_turn(self.player_2)
        else:
            pass


    def get_player_score(self, player):
        return len(list(filter(lambda player_win: player_win == player, self.game_wins)))
    
    

    def print_title(self):
        print(f"  {self.mode}  \n\nNaughts and Crosses\n")
        
    def print_scoreboard(self):
        if len(self.game_wins) > 0:
            print(f" {self.player_1}: {self.get_player_score(self.player_1)}  VS {self.player_2}: {self.get_player_score(self.player_2)} \n\n")
    

    def initiate_and_validate_player_turn(self, current_player):
        is_valid = False
        placement = None
        prompt_count = 0
        if self.games_played > 0 and self.board.box == [" ", " ", " ", " ", " ", " ", " ", " ", " "]:
            os.system("clear")
            print(f"{current_player} you go first this round")
            time.sleep(2)
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
            is_valid = self.board.is_valid_placement(placement)
            prompt_count += 1
           

        self.board.update_boxes(int(placement) - 1, marker)
        return self.validate_player_win(current_player, marker)

    def validate_player_win(self, current_player, marker):
        current_player_wins = self.board.win_game(marker)
        if current_player_wins:
            self.game_wins.append(current_player)
        else:
            pass

        return current_player_wins
    
    def bot_talk(self, chatter):
        chatter_count = random.randint(1, 2)
        while chatter_count != 0:
            chatter_count -= 1
            self.refresh_gamescreen()
            print("\n" + chatter[random.randint(0, (len(chatter) - 1))])
            if self.player_2 == 'Drunk Uncle':
                time.sleep(random.randint(1, 3))
            elif self.player_2 == 'Chucky':
                time.sleep(2)


    def initiate_and_validate_bot_turn(self): 
        bot_placement = 0
        self.refresh_gamescreen()
        if self.player_2 == 'Drunk Uncle':
            chatter = ["hmmmm...", "(Grunting)", "uuuuuuuggggghhhhh", "*scratches scrotom and sniffs fingers*", "hucks loogie and spits it", "hassle's onlooker", "starts rambling about hardships of his childhood", "starts a longwinded story that you've heard 6+ times"]
            self.bot_talk(chatter)
            while True:
                bot_placement = random.randint(1,9)
                if self.board.is_valid_placement(str(bot_placement)):
                    break

            # ...do drunk uncle turn code in differenbt method for clean code
        elif self.player_2 == 'Chucky':
            chatter = ["Mwahahaha",  "It might be Game Over for you", "*cackles*", "*starts sharpenening your kitchen knife that went missing*", "*throws tomohawk and closely misses onlooker*"]
            self.bot_talk(chatter)
            while True:
                bot_placement = random.randint(1,9)
                if self.board.is_valid_placement(str(bot_placement)):
                    break
            # ...do chucky turn code in differenbt method for clean code
        
        self.board.update_boxes(bot_placement - 1, 'O')
        return self.validate_player_win(self.player_2, 'O')

    def on_tie_game(self): 
        self.refresh_gamescreen()
        print ("\nTie game\n")
        self.on_game_finished()

    def on_player_win(self, winning_player): 
        self.refresh_gamescreen()
        print(f"{winning_player} wins!\n")
        self.on_game_finished()


    def on_game_finished(self):
        self.games_played += 1
        rematch = input("Would you like to play again? (Y/N): ").lower()
        if rematch == "y":
            self.rematch()
            
        else:
            self.game_wins = []
            self.games_played = 0
            self.rematch()
            return self.choose_mode()

    def pvp(self):
        ordered_players = [self.player_2, self.player_1] if self.games_played % 2 else [self.player_1, self.player_2]
        # check for player 1 win
        while True: 
            for player in ordered_players:
                players_wins = False

                if self.versus_bot and self.player_2 == player:
                    players_wins = self.initiate_and_validate_bot_turn()
                else:
                    players_wins = self.initiate_and_validate_player_turn(player)
                    

                if players_wins: 
                    self.on_player_win(player)

                if self.board.tie_game():
                    self.on_tie_game()
   


           