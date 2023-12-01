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
    for input in inputs:
        nums = re.findall(r'\d', input)
        total += (int(nums[0]) * 10 + int(nums[-1]))
    return total

if __name__ == "__main__":
    main()
