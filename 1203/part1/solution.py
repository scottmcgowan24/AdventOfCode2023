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
    # Locations of the symbols on the previous line
    prev_symbol_locations = []

    # Locations of the numbers on the previous line
    prev_numbers = [] # May have to store extra data since numbers can be more than one character

    for input in inputs:
        # Get the locations of all the numbers
        number_matches = re.finditer(r'\d+', input)
        number_locations = []
        for num in number_matches:
            number_locations.append([num.start(), num.end(), int(num.group()), 0]) # Last entry indicates if the number has been counted

        # Get the locations of all the symbols
        symbol_matches = re.finditer(r'[^0-9.]', input)
        symbol_locations = []
        for val in symbol_matches:
            symbol_locations.append(val.start())

        # From here, we check for three situations:
        # 1. Symbols that are next to the numbers in this row
        # 2. Symbols that are above the numbers in this row (Check current numbers to previous symbols)
        # 3. Symbols that are below the numbers in this rot (Do backtrack, check previous numbers to current symbols)

        for num in number_locations:
            # Number 1 check
            for loc in range(num[0]-1, num[1] +1):
                if loc in symbol_locations and not num[3]:
                    total += num[2]
                    num[3] = 1
                    break

            # Number 2 check
            for loc in range(num[0]-1, num[1] +1):
                if loc in prev_symbol_locations and not num[3]:
                    total += num[2]
                    num[3] = 1
                    break
            
        # Number 3 check
        for num in prev_numbers:
            for loc in range(num[0]-1, num[1] +1):
                if loc in symbol_locations and not num[3]:
                    total += num[2]
                    num[3] = 1
                    break
        
        prev_numbers = number_locations
        prev_symbol_locations = symbol_locations
    return total

if __name__ == "__main__":
    main()
