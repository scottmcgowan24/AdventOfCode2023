#!/usr/bin/env python3
import re

def main():
    file_path = 'input.txt'

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            inputs = []

            for line in lines:
                inputs.append(line.strip())

            solution = sol(inputs)
            print(solution)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def sol(inputs):
    powerSum = 0
    for input in inputs:
        min_possible = [0, 0, 0]
        tokens = re.split(r'[:;]', input)
        for grab in range(1, len(tokens)):
            # Iterate over the grabs and see if the grab is possible. If not just move along to the next game
            grabPowers = get_power(tokens[grab])
            min_possible[0] = max(grabPowers[0], min_possible[0])
            min_possible[1] = max(grabPowers[1], min_possible[1])
            min_possible[2] = max(grabPowers[2], min_possible[2])
        power = min_possible[0] * min_possible[1] * min_possible[2]
        powerSum += min_possible[0] * min_possible[1] * min_possible[2]
    return powerSum

def get_power(grab):
    min_possible = {
        "red" : 0,
        "green": 0,
        "blue": 0
    }
    colors = re.findall(r'blue|red|green', grab)
    numbers = re.findall(r'\d+', grab)
    for i in range(len(colors)):
        min_possible[colors[i]] = max(min_possible.get(colors[i]), int(numbers[i]))
    return [min_possible["red"], min_possible["blue"], min_possible["green"]]


if __name__ == "__main__":
    main()
