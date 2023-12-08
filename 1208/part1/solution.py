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
    directions = list(inputs[0])
    network = {} # Will fill with necessary info
    for input in inputs[1:]:
        coordinates = re.findall(r'[a-zA-Z]{3}', input)
        network[coordinates[0]] = (coordinates[1], coordinates[2])
    
    # Now that we have the network defined, just start at AAA and rip it until 
    # we get to ZZZ
    current_location = "AAA"
    total_steps = 0
    while True:
        direction = directions[total_steps % len(directions)]
        if direction == "L":
            current_location = network.get(current_location)[0]
        else:
            current_location = network.get(current_location)[1]
        total_steps += 1
        if current_location == "ZZZ":
            return total_steps

if __name__ == "__main__":
    main()
