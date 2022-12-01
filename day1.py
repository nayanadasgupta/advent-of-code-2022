from aocd import lines
import heapq


def get_calories_per_elf(input):
    caloriesCarriedPerElf = []
    currentSum = 0
    for item in input:
        if item == '':
            caloriesCarriedPerElf.append(currentSum)
            currentSum = 0
        else:
            currentSum += int(item)
    return caloriesCarriedPerElf


def mostCaloriesCarried(input):
    return max(get_calories_per_elf(input))


def threeHighestCaloriesCarried(input):
    return sum(heapq.nlargest(3, get_calories_per_elf(input)))


print("---- Part 1 ----")
print(mostCaloriesCarried(lines))
print("---- Part 2 ----")
print(threeHighestCaloriesCarried(lines))
