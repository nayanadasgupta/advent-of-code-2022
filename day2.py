
def get_move_score(move):
    key = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    return key[move]


def decode_move(encoded_move):
    key = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }
    return key[encoded_move]


def get_result(opponent_move, my_move):
    if opponent_move == my_move:
        return ("Draw", 3)
    if opponent_move == "Rock":
        if my_move == "Paper":
            return ("Win", 6)
        elif my_move == "Scissors":
            return ("Loss", 0)
    elif opponent_move == "Paper":
        if my_move == "Rock":
            return ("Loss", 0)
        elif my_move == "Scissors":
            return ("Win", 6)
    elif opponent_move == "Scissors":
        if my_move == "Rock":
            return ("Win", 6)
        elif my_move == "Paper":
            return ("Loss", 0)


def total_score(strategy_guide):
    lines = [line.rstrip() for line in strategy_guide]
    results = []
    for line in lines:
        encoded_opponent_move, encoded_my_move = line.split(" ")
        opponent_move, my_move = decode_move(
            encoded_opponent_move), decode_move(encoded_my_move)
        results.append(get_result(opponent_move, my_move)
                       [1] + get_move_score(my_move))
    return sum(results)


def decide_move(opponent_move, result):
    if result == "Draw":
        return opponent_move
    elif result == "Win":
        if opponent_move == "Rock":
            return "Paper"
        elif opponent_move == "Scissors":
            return "Rock"
        elif opponent_move == "Paper":
            return "Scissors"
    elif result == "Loss":
        if opponent_move == "Rock":
            return "Scissors"
        elif opponent_move == "Scissors":
            return "Paper"
        elif opponent_move == "Paper":
            return "Rock"


def total_sneaky_score(strategy_guide):
    lines = [line.rstrip() for line in strategy_guide]
    results = []
    for line in lines:
        encoded_opponent_move, encoded_result = line.split(" ")
        opponent_move, result = decode_move(
            encoded_opponent_move), decode_end_result(encoded_result)
        my_move = decide_move(opponent_move, result)
        results.append(get_result(opponent_move, my_move)
                       [1] + get_move_score(my_move))
    return sum(results)


def decode_end_result(encoded):
    key = {
        "X": "Loss",
        "Y": "Draw",
        "Z": "Win"
    }
    return key[encoded]


if __name__ == "__main__":
    with open("data/day2.txt") as file:
        print(total_sneaky_score(file))
