def process_input(lines):
    pairs = []
    for pair in lines:
        pairs.append([map(int, assignment.split("-"))
                     for assignment in pair.split(",")])
    return pairs


def part_1(lines):
    num_fully_contained_pairs = 0
    for pair in lines:
        left, right = pair.split(",")
        left_start, left_end = map(int, left.split("-"))
        right_start, right_end = map(int, right.split("-"))
        if (left_start <= right_start and left_end >= right_end) or (right_start <= left_start and right_end >= left_end):
            num_fully_contained_pairs += 1
            # print(left_start, left_end, right_start, right_end)
    print("Part 1:", num_fully_contained_pairs)


def part_2(lines):
    num_overlapping_pairs = 0
    for pair in lines:
        left, right = pair.split(",")
        left_start, left_end = map(int, left.split("-"))
        right_start, right_end = map(int, right.split("-"))
        if max(left_start, right_start) <= min(left_end, right_end):
            num_overlapping_pairs += 1
    print("Part 2:", num_overlapping_pairs)


if __name__ == "__main__":
    with open("data/sample_day4.txt") as file:
        lines = [line.rstrip() for line in file]
        part_1(lines)
        part_2(lines)
        # process_input(lines)
