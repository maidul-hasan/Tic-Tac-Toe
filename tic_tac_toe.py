import random
import time

choices_made = {item: "" for item in range(1, 10)}
signs = [(1, "X"), (2, "O")]
player01_sign = []


class HumanPlayer:
    def __init__(self, player_name):
        self.player_name = player_name
        self.sign = ""

    def get_turn(self):
        print(f"It's the turn of {self.player_name}. Please Enter (1~9) to select a position: ", end="")
        while True:
            try:
                position = int(input())
                if 0 < position < 10:
                    try:
                        if choices_made[position] == "":
                            choices_made.update({position: self.sign})
                            break
                        elif choices_made[position] != "":
                            print("This position was previously selected. Please select a new position: ", end="")
                            continue
                    except KeyError:
                        choices_made.update({position: self.sign})
                        break
                else:
                    print("Enter values that are in the range of (1~9): ", end="")
                    continue
            except ValueError:
                print("Please Enter a value between (1~9) not some gibberish: ", end="")


class ComputerPlayer:
    def __init__(self, player_name):
        self.player_name = player_name
        self.sign = ""

    def get_turn(self):
        computer_attempt = "not played yet"
        print(f"It's the turn of {self.player_name}.", end="")
        while True:
            try:
                win_combs = win_combinations()
                for win_comb in win_combs:
                    temp_lst = []
                    for item in win_comb:
                        temp_lst.append(choices_made[item])
                        if temp_lst.count(player01_sign[0]) == 2 and temp_lst.count(self.sign) == 0 and choices_made[
                            item] == "":
                            choices_made.update({item: self.sign})
                            print(f"{self.player_name} selected the position {item}.")
                            computer_attempt = "played"
                            break
                    if computer_attempt == "played":
                        break
                rand_pos = random.randint(1, 9)
                if choices_made[rand_pos] == "" and computer_attempt == "not played yet":
                    choices_made.update({rand_pos: self.sign})
                    print(f"{self.player_name} selected the position {rand_pos}.")
                    break
                elif choices_made[rand_pos] != "" and computer_attempt == "not played yet":
                    continue
            except:
                pass
            else:
                break


def init_board():
    for item in range(1, 10):
        print("|\t", item, "\t", "|", end="")
        if item != 1 and item % 3 == 0:
            print("\n", "-" * 24)


def show_board():
    for key, value in choices_made.items():
        print("|\t", value, "\t", "|", end="")
        if key != 1 and key % 3 == 0:
            print("\n", "-" * 24)


def clear_board():
    for key in choices_made.keys():
        choices_made.update({key: ""})
    signs.clear()
    signs.extend([(1, "X"), (2, "O")])
    player01_sign.clear()


def chose_player():
    print("Who do you want to play against? (1. A Human player or, 2. The Computer): ", end="")
    while True:
        try:
            response = int(input())
            if response == 1:
                player_type = "human_player"
                return player_type
            elif response == 2:
                player_type = "computer_player"
                return player_type
            else:
                print("Please select a valid option (1/2): ", end="")
                continue
        except ValueError:
            print("Please Enter (1/2) to select from the options: ", end="")


def win_combinations():
    k_lst = list(choices_made.keys())
    zip_lst = list(zip(k_lst[0:3], k_lst[3:6], k_lst[6:9]))
    win_combs = []
    win_combs.extend([k_lst[0:3], k_lst[3:6], k_lst[6:9], [1, 5, 9], [3, 5, 7]])
    for item in zip_lst:
        win_combs.append(item)
    return win_combs


def get_winner():
    win_combs = win_combinations()
    for win_comb in win_combs:
        temp_lst = []
        for item in win_comb:
            temp_lst.append(choices_made[item])
        if temp_lst.count("X") == 3:
            return "X"
        elif temp_lst.count("O") == 3:
            return "O"
        elif list(choices_made.values()).count("X") >= 4 and list(choices_made.values()).count("O") >= 4:
            return "Draw"


def welcome():
    print("""\n\n
                        WELCOME TO THE GAME OF 
                    ==============================
                              TIC TAC TOE
                    ==============================
                    """)
    time.sleep(1)

    # showing the initial board positions
    print(
        "\n***  A num-pad is used to denote the positions of the board. Enter a number (1~9) to place your sign at the "
        "respective position on the board.  ***\nThe num-pad looks like this - ")
    init_board()


def play():
    # Creating the main player
    global opponent
    while True:
        player_name = input("Enter your name: ")
        if len(player_name) == 0:
            print("Please enter a valid name. ", end="")
        else:
            break
    player = HumanPlayer(player_name)
    while True:
        print("Which sign do you want to use? (1. 'X' 2. 'O'): ", end="")
        try:
            player_sign = int(input())
            if player_sign == 1:
                player.sign = signs[0][1]
                player01_sign.append(signs[0][1])
                signs.pop(0)
                break
            elif player_sign == 2:
                player.sign = signs[1][1]
                player01_sign.append(signs[1][1])
                signs.pop(1)
                break
            else:
                print("Please select a valid option. ", end="")
                continue
        except ValueError:
            print("Please Enter (1/2) to select from the options. ", end="")

    # Creating the opponent player
    opponent_type = chose_player()
    if opponent_type == "human_player":
        while True:
            opponent_name = input("Enter a name for your opponent Player: ")
            if len(opponent_name) == 0:
                print("Please Enter a valid name. ", end="")
            else:
                break
        opponent = HumanPlayer(opponent_name)
        opponent.sign = signs[0][1]
    elif opponent_type == "computer_player":
        opponent = ComputerPlayer("Computer")
        opponent.sign = signs[0][1]

    # determining who gets the first turn
    board_turn = ["_"]
    while True:
        try:
            response = int(input("Flipping coin (1. Head or 2. Tails). What do you chose? : "))
            if response > 2 or response < 1:
                print("Please select a valid option. ", end="")
                continue
            else:
                break
        except ValueError:
            print("Enter (1/2) to select from the options.", end="")

    rand = random.randint(1, 2)
    if response == rand:
        print("Congratulations! you get to go first.")
        board_turn[0] = "player"
    elif response != rand:
        print("Sorry :( your opponent gets to go first.")
        board_turn[0] = "opponent"

    # playing by turn
    for _ in range(9):
        if board_turn[0] == "player":
            player.get_turn()
            board_turn[0] = "opponent"
            show_board()

        else:
            opponent.get_turn()
            board_turn[0] = "player"
            show_board()

        if get_winner() == player.sign:
            print(f"{player.player_name} has Won the game!")
            break
        elif get_winner() == opponent.sign:
            print(f"{opponent.player_name} has Won the game!")
            break
        elif get_winner() == "Draw":
            print(":( It's a Draw.")
            break
        else:
            continue


def replay():
    print("\n\n\nDo you want to play again? (1. Yes 2. No): ", end="")
    while True:
        try:
            choice = int(input())
            if choice < 1 or choice > 2:
                print("Please enter (1/2): ", end="")
                continue
            else:
                break
        except ValueError:
            print("Enter (1/2) to select from the options: ", end="")
    if choice == 1:
        return True
    elif choice == 2:
        return False


def start_playing():
    while True:
        welcome()
        play()
        clear_board()
        if not replay():
            break


start_playing()
