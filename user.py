from table import Table

class Game:
    def __init__(self):
        self.x = "x"
        self.o = "o"    

    def if_win(self, the_table):
        if the_table[0] == the_table[1] == the_table[2] == "x":
            return True
        elif the_table[3] == the_table[4] == the_table[5] == "x":
            return True   
        elif the_table[6] == the_table[7] == the_table[8] == "x":
            return True
        elif the_table[0] == the_table[3] == the_table[6] == "x":
            return True
        elif the_table[1] == the_table[4] == the_table[7] == "x":
            return True
        elif the_table[2] == the_table[5] == the_table[8] == "x":
            return True
        elif the_table[0] == the_table[4] == the_table[8] == "x":
            return True
        elif the_table[2] == the_table[4] == the_table[6] == "x":
            return True
        elif the_table[0] == the_table[1] == the_table[2] == "o":
            return True
        elif the_table[3] == the_table[4] == the_table[5] == "o":
            return True   
        elif the_table[6] == the_table[7] == the_table[8] == "o":
            return True
        elif the_table[0] == the_table[3] == the_table[6] == "o":
            return True
        elif the_table[1] == the_table[4] == the_table[7] == "o":
            return True
        elif the_table[2] == the_table[5] == the_table[8] == "o":
            return True
        elif the_table[0] == the_table[4] == the_table[8] == "o":
            return True
        elif the_table[2] == the_table[4] == the_table[6] == "o":
            return True


    def draw_table(self,the_table):
        return f"|1:{the_table[0]}|2:{the_table[1]}|3:{the_table[2]}|\n|4:{the_table[3]}|5:{the_table[4]}|6:{the_table[5]}|\n|7:{the_table[6]}|8:{the_table[7]}|9:{the_table[8]}|"

    def run(self):
        run_game = Table()
        start = True
        while start:
            user = 0
            while user == 0:
                change = run_game.change_table(user = self.x, available_list=run_game.available, used_list=run_game.used)
                win = self.if_win(list(run_game.run_table(change)))
                if win == True:
                    
                    print("\nBOARD")                      
                    print(self.draw_table(list(run_game.run_table(change))))
                    print(f"\nPlayer {self.x.upper()} won!\n")
                    print()
                    start = False
                    user = 2
                
                elif "-" not in list(run_game.run_table(change)):
                    print("\nDRAW\n")
                    print(self.draw_table(list(run_game.run_table(change))))
                    user = 2
                    start = False
                    
                else:
                    print(f"\nTurn of player ({self.o.upper()})! \n")
                    print("BOARD")                    
                    print(self.draw_table(list(run_game.run_table(change))))
                    print()
                    user = 1
            
            while user == 1:
                change = run_game.change_table(user = self.o, available_list=run_game.available, used_list=run_game.used)
                win = self.if_win(list(run_game.run_table(change)))
                if win == True:

                    print("\nBOARD")                     
                    print(self.draw_table(list(run_game.run_table(change))))
                    print(f"\nPlayer {self.o.upper()} won!\n")
                    start = False
                    user = 2
                elif "-" not in list(run_game.run_table(change)):
                    print("\nDRAW\n")
                    user = 2
                    start = False
                else:
                    print(f"\nTurn of player ({self.x.upper()})!\n")
                    print("")
                    print("BOARD")
                    print(self.draw_table(list(run_game.run_table(change))))
                    print()
                    user = 0
        
        return "\nEnd Game"

if __name__ == "__main__":
    game = Game()
    print(game.run())
    



