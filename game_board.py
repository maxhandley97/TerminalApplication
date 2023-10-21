class Board:
    def __init__(self):
        self.box = self.create_box()

    def create_box(self): #creates new array for multiple games
        return  [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def restart_board(self): 
        self.box = self.create_box()

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
