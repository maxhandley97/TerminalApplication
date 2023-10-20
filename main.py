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
        print(" " + self.box[6] + " | " + self.box[7] + " | " + self.box[8])
    
    def update_boxes(self, box_number, player):
        if self.box[box_number] == " ":
            self.box[box_number] = player

class GameController:
    def __init__(self):
        self.board = Board()
        self.mode = 'PVP'

    def choose_mode(self):
        choice = int(input("""              Let the games begin... \n\n To continue, choose from the following game modes:\n
              Player vs Player (1) \n
              Player vs Uncle (2) \n
              Player vs Chucky (3) \n\n"""))
        if choice = 1:


        

    def print_title(self):
        print(" PVP \n Naughts and Crosses")

    def clear_screen(self):
        os.system("clear")
        self.print_title()
        self.board.gameboard()
    
    def pvp(self):
        while True: 
            game.clear_screen()
            x_placement = int(input("\n Player X please choose 1-9"))
            move = x_placement - 1



game = GameController()

game.choose_mode()









