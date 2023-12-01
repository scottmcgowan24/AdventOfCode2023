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
        pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
        matches = re.finditer(f'(?=({pattern}))', input)
        nums = [match.group(1) for match in matches]
        nums_map = {
            "one" : 1,
            "two" : 2,
            "three" : 3,
            "four" : 4,
            "five" : 5,
            "six" : 6,
            "seven" : 7,
            "eight" : 8,
            "nine" : 9
        }
        try:
            firstNum = int(nums[0]) * 10
        except ValueError:
            firstNum = nums_map.get(nums[0]) * 10
        
        try:
            lastNum = int(nums[-1])
        except ValueError:
            lastNum = nums_map.get(nums[-1])
        total += (firstNum + lastNum)
    return total

if __name__ == "__main__":
    main()
