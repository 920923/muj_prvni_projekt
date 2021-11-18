import os
import sys

game_area_dict = {"1": " ", "2": " ", "3": " ",
                  "4": " ", "5": " ", "6": " ",
                  "7": " ", "8": " ", "9": " "}


def hlavni():
    rules_game()


def rules_game():
    print(separator := "-" * 40)
    print(f"WELCOME TO TIC TAC TOE".center(len(separator)), separator, sep="\n")
    print(f"GAME RULES:".center(len(separator)))
    print(f"""Each player can place one mark (or stone) 
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row"""
          )
    print(spearator_2 := "=" * 40, "Let’s start the game".center(len(separator)), separator, sep="\n")
    start_game()


def start_game():  # def round_continue(player, number_of_moves)
    player = "X"
    game_round = 0
    while True:
        game_area(game_area_dict)
        print(separator := "=" * 51)
        move: str = input(f"Player: {player}, | Pleas enter your move nuber (1-9):")
        # delete()
        if move.isnumeric() and game_area_dict[move] == " ":
            game_area_dict[move] = player
            game_round = game_round + 1  # format number_of_moves += number_of_moves NEFUNGUJE!
            if game_round == 9:
                print("Game over, TIE!")
                quit()
            control_win(player)
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("Wrong number (1-9) or this place is already filled, enter your number again")


def control_win(player):
    if game_area_dict["1"] == game_area_dict["2"] == game_area_dict["3"] != " ":  # horizontal top
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["4"] == game_area_dict["5"] == game_area_dict["6"] != " ":  # horizontal middle
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["7"] == game_area_dict["8"] == game_area_dict["9"] != " ":  # horizontal bot
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["1"] == game_area_dict["4"] == game_area_dict["7"] != " ":  # vertical left
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["2"] == game_area_dict["5"] == game_area_dict["8"] != " ":  # vertical middle
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["3"] == game_area_dict["6"] == game_area_dict["9"] != " ":  # vertical right
        game_area(game_area_dict)
        print(f"Game over, player ", player, "won.")
        quit()
    elif game_area_dict["1"] == game_area_dict["5"] == game_area_dict["9"] != " ":  # diagonal 1
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()
    elif game_area_dict["3"] == game_area_dict["5"] == game_area_dict["7"] != " ":  # diagonal 2
        game_area(game_area_dict)
        print(f"Game over, player", player, "won.")
        quit()


def game_area(area):
    print("+---+---+---+")
    print(f"|", area["1"], "|", area["2"], "|", area["3"], "|")
    print("+---+---+---+")
    print(f"|", area["4"], "|", area["5"], "|", area["6"], "|")
    print("+---+---+---+")
    print(f"|", area["7"], "|", area["8"], "|", area["9"], "|")
    print("+---+---+---+")


def os_windows():
    return sys.platform == "Windows"


def delete():
    if os_windows():
        os.system("clear")
    else:
        os.system("cls")


hlavni()

# print(
# f"+---+---+---+".center(len(separator)), "\n"
# "|", area["1"], "|", area["2"], "|", area["3"], "|", "\n"
# "+---+---+---+", "\n"
# "|", area["4"], "|", area["5"], "|", area["6"], "|", "\n"
# "+---+---+---+", "\n"
# "|", area["7"], "|", area["8"], "|", area["9"], "|", "\n"
# "+---+---+---+"
# )

#     separator = "-" * 40
#     print("""
#     +---+---+---+
#     |   |   |   |
#     +---+---+---+
#     |   |   |   |
#     +---+---+---+
#     |   |   |   |
#     +---+---+---+
#     """)
