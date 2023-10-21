import os
os.system("clear")

class Board:
    def __init__(self):
        self.box = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def gameboard(self):
        print(" " + self.box[0] + " | " + self.box[1] + " | " + self.box[2])
        print("-----------")
        print(" " + self.box[3] + " | " + self.box[4] + " | " + self.box[5])
        print("-----------")
        print(" " + self.box[6] + " | " + self.box[7] + " | " + self.box[8] + "\n")
    
    def update_boxes(self, box_number, player):
        if self.box[box_number] == " ":
            self.box[box_number] = player

    def win_game(self, player):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        for win in win_combinations:
            if self.box[win[0]] == self.box[win[1]] == self.box[win[2]] == player:
                return True
        return False


class GameController:
    def __init__(self):
        self.board = Board()
        self.mode = 'PVP'
    
    def turn_on_game(self):
        pass

    def choose_mode(self):
        name_1 = input("Please enter your name: ")
        choice = int(input("""              Let the games begin... \n\n To continue, choose from the following game modes:\n
              Player vs Player (1) \n
              Player vs Uncle (2) \n
              Player vs Chucky (3) \n\n"""))
        if choice == 1:
            self.mode = 'PVP'
            return self.start_game()
        elif choice == 2:
            pass
        
    def refresh_gamescreen(self):
        os.system("clear")
        self.print_title()
        self.board.gameboard()
    

    def start_game(self): 
        if self.mode == 'PVP':
            return self.pvp()
        

    def print_title(self):
        print(f"   {self.mode} \n\nNaughts and Crosses\n")

        
        
    def pvp(self):
        while True: 
            self.refresh_gamescreen()
            x_placement = int(input("\n Player X please choose 1-9: "))
            move_x = x_placement - 1
            self.board.update_boxes(move_x, "X")

            if self.board.win_game("X"): 
                print(f"X player wins!\n")
                break


            self.refresh_gamescreen()
            o_placement = int(input("\n Player O please choose 1-9: "))
            move_o = o_placement - 1
            self.board.update_boxes(move_o, "O")

            if self.board.win_game("X"): 
                print(f"Player wins!\n")
                break
        

           
        
            




game = GameController()

game.choose_mode()









