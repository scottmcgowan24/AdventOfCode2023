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
    total = 0
    # Go through the different histories and begin extrapolation
    for input in inputs:
        initial_history = re.findall(r'-?\d+', input)
        print(initial_history)
        new_value = predict([int(value) for value in reversed(initial_history)])

        total += new_value
    return total

def predict(current_list):
    if all(value == 0 for value in current_list):
        return 0 # Base case

    steps = [final - initial for initial, final in zip(current_list, current_list[1:])]
    value = current_list[-1] + predict(steps) # Add last value + whatever the step should be
    return value

if __name__ == "__main__":
    main()
