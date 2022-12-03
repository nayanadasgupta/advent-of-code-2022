def get_shared_item(rucksack):
    half = len(rucksack) // 2
    first_half, second_half = rucksack[:half], rucksack[half:]
    return set(first_half).intersection(second_half)


def get_priority(item):
    if item.islower():
        return ord(item) - (ord('a') - 1)
    return ord(item) - (ord('A') - 27)


def part_1(lines):
    result = []
    for line in lines:
        shared_items = get_shared_item(line)
        for item in shared_items:
            result.append(get_priority(item))
    print("Part 1:", sum(result))


def get_shared_badge(group_rucksacks):
    return (set(group_rucksacks[0]) & set(group_rucksacks[1]) & set(group_rucksacks[2])).pop()


def part_2(lines):
    grouped_lines = []
    for i in range(0, len(lines), 3):
        grouped_lines.append([lines[i], lines[i+1], lines[i+2]])
    shared_badges = []
    for group in grouped_lines:
        shared_badges.append(get_shared_badge(group))
    print("Part 2:", sum(map(lambda badge: get_priority(badge), shared_badges)))


if __name__ == "__main__":
    with open("data/day3.txt") as file:
        lines = [line.rstrip() for line in file]
        part_1(lines)
        part_2(lines)
