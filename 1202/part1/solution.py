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
    idSum = 0
    for input in inputs:
        is_possible = True
        tokens = re.split(r'[:;]', input)
        # Probably can just increment a counter, but I don't trust the input to give consistent numbers
        gameId = int(re.search(r'\d+', tokens[0]).group())
        for grab in range(1, len(tokens)):
            # Iterate over the grabs and see if the grab is possible. If not just move along to the next game
            if not possible(tokens[grab]):
                is_possible = False
                break

        if is_possible:
            idSum += gameId
    return idSum

def possible(grab):
    possible_map = {
        "red" : 12,
        "green": 13,
        "blue": 14
    }
    colors = re.findall(r'blue|red|green', grab)
    numbers = re.findall(r'\d+', grab)
    for i in range(len(colors)):
        if int(numbers[i]) > possible_map.get(colors[i]):
            return False
    return True


if __name__ == "__main__":
    main()
