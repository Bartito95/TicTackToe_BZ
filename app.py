from user import Game

def is_string():
    insert = str(input("\nWould you like to continue the game? [Y/N]? "))
    if insert.lower() in ["y", "n"]:
        if insert.lower() == "y":
            print("\nGreat, let's play again!")
            return insert.lower()
        elif insert.lower() == "n":
            print("\nNo problem, maybe next time. See ya!")
            return insert.lower()
    else:
        return is_string()
            
if __name__ == "__main__":
    game = Game()
    start_game = "y"

    while start_game == "y":
        print("Player X starts!")
        print(game.run())
        start_game = is_string()
