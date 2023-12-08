#!/usr/bin/env python3
import re
import math

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
    
    current_starting_locations = [entry for entry in network.keys() if entry[2] == "A"]
    individual_answers = []
    for starting_location in current_starting_locations:
        location = starting_location
        total_steps = 0
        while True:
            direction = directions[total_steps % len(directions)]
            if direction == "L":
                location = network.get(location)[0]
            else:
                location = network.get(location)[1]
            total_steps += 1
            if location[2] == "Z":
                individual_answers.append(total_steps)
                break
    return math.lcm(*individual_answers) # Unpacking a list into separate arguments, super cool!

if __name__ == "__main__":
    main()
