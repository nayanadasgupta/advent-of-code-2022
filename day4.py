def process_input(pair):
    left, right = pair.split(",")
    left_start, left_end = map(int, left.split("-"))
    right_start, right_end = map(int, right.split("-"))
    return left_start, left_end, right_start, right_end


def part_1(lines):
    num_fully_contained_pairs = 0
    for pair in lines:
        left_start, left_end, right_start, right_end = process_input(pair)
        if (left_start <= right_start and left_end >= right_end) or (right_start <= left_start and right_end >= left_end):
            num_fully_contained_pairs += 1
    print("Part 1:", num_fully_contained_pairs)


def part_2(lines):
    num_overlapping_pairs = 0
    for pair in lines:
        left_start, left_end, right_start, right_end = process_input(pair)
        is_overlapping = max(left_start, right_start) <= min(
            left_end, right_end)
        if is_overlapping:
            num_overlapping_pairs += 1
    print("Part 2:", num_overlapping_pairs)


if __name__ == "__main__":
    with open("data/day4.txt") as file:
        lines = [line.rstrip() for line in file]
        part_1(lines)
        part_2(lines)
