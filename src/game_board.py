from colorama import init
init()
from termcolor import colored
class Board:
    def __init__(self):
        self.box = self.create_box()

    def create_box(self): #creates new array for multiple games
        return  [" ", " ", " ", " ", " ", " ", " ", " ", " "] 
        # return [" ", "O", "X", "O", "O", "X", "X", "X", "O"]
        # return ["X", "X", " ", "O", "O", " ", " ", " ", " "]

    def is_valid_placement(self, placement):
        return placement.isdigit() and (int(placement) >= 1 and int(placement) <= 9) and self.box[int(placement) - 1] == " "

    
    def restart_board(self): 
        self.box = self.create_box()

    def gameboard(self):
        gameboard = (" " + self.box[0] + " | " + self.box[1] + " | " + self.box[2] + "\n"
        "-----------\n"
        " " + self.box[3] + " | " + self.box[4] + " | " + self.box[5] + "\n"
        "-----------\n"
        " " + self.box[6] + " | " + self.box[7] + " | " + self.box[8] + "\n")
        print(gameboard)
    
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
    
    def tie_game(self):
        return " " not in self.box

