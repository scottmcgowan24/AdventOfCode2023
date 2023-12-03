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
    prev_stars = []

    # Locations of the numbers on the previous line
    prev_numbers = [] # May have to store extra data since numbers can be more than one character

    for input in inputs:
        # Get the locations of all the numbers
        number_matches = re.finditer(r'\d+', input)
        number_locations = []
        for num in number_matches:
            number_locations.append([num.start(), num.end(), int(num.group())])

        # Get the locations of all the stars
        symbol_matches = re.finditer(r'\*', input)
        star_locations = []
        for val in symbol_matches:
            star_locations.append([val.start(), []]) # Second entry is a list of the numbers adjacent to this star

        # From here, we check for three situations:
        # 1. Numbers which are adjacent to this star in this row
        # 2. Numbers which are above this star
        # 3. Numbers which are below this star
        # Once we are done, we can always count the previous star list's numbers and go from there. 

        for star in star_locations:
            # Number 1
            for num in number_locations:
                if (star[0] == num[0] - 1) or (star[0] == num[1]):
                    star[1].append(num[2])
            
            # Number 2
            for num in prev_numbers:
                for loc in range(num[0]-1, num[1] +1):
                    if loc == star[0]:
                        star[1].append(num[2])
                        break
        
        # Number 3
        for star in prev_stars:
            for num in number_locations:
                for loc in range(num[0]-1, num[1] +1):
                    if loc == star[0]:
                        star[1].append(num[2])
                        break
        # Now we go through the previous list of stars before overwriting them and if they have 
        # Exactly two numbers in their list, multiple them and add to the total.
        for star in prev_stars:
            if len(star[1]) == 2:
                total += (star[1][0] * star[1][1])
        prev_numbers = number_locations
        prev_stars = star_locations
    return total

if __name__ == "__main__":
    main()
