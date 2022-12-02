
def get_move_score(move):
    key = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    return key[move]


def get_game_result(opponent_move, my_move):
    if opponent_move == my_move:
        return 3
    elif (opponent_move == "Paper" and my_move == "Scissors") or (opponent_move == "Rock" and my_move == "Paper") or (opponent_move == "Scissors" and my_move == "Rock"):
        return 6
    else:
        return 0


decode_move = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}


def part_1(lines):
    results = []
    for line in lines:
        opponent_move, my_move = [decode_move[x] for x in line.split(" ")]
        results.append(get_game_result(
            opponent_move, my_move) + get_move_score(my_move))
    return sum(results)


def decide_move(opponent_move, expected_result):
    if expected_result == "Draw":
        return opponent_move
    if opponent_move == "Rock":
        return "Paper" if expected_result == "Win" else "Scissors"
    if opponent_move == "Scissors":
        return "Rock" if expected_result == "Win" else "Paper"
    if opponent_move == "Paper":
        return "Scissors" if expected_result == "Win" else "Rock"


def part_2(lines):
    decode_result = {
        "X": "Loss",
        "Y": "Draw",
        "Z": "Win"
    }
    results = []

    for line in lines:
        encoded_opponent_move, encoded_result = line.split(" ")
        opponent_move, result = decode_move[
            encoded_opponent_move], decode_result[encoded_result]
        my_move = decide_move(opponent_move, result)
        results.append(get_game_result(
            opponent_move, my_move) + get_move_score(my_move))
    return sum(results)


if __name__ == "__main__":
    with open("data/day2.txt") as file:
        lines = [line.rstrip() for line in file]
        print("Part 1:", part_1(lines))
        print("Part 2:", part_2(lines))

        assert part_1(lines) == 11906
        assert part_2(lines) == 11186
        print("Assertions passed")
