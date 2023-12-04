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
        actual_values = input.split(':')
        split_nums = actual_values[1].split('|')
        winning_nums = re.findall(r'\d+', split_nums[0])
        ticket_nums = re.findall(r'\d+', split_nums[1])
        matching_nums = list(set(winning_nums).intersection(ticket_nums))
        if len(matching_nums) > 0:
            total += 2 ** (len(matching_nums) - 1)

    return total
if __name__ == "__main__":
    main()
