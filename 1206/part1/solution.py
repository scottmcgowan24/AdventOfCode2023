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
    total_solutions = 1
    times = re.findall(r'\d+', inputs[0])
    distances = re.findall(r'\d+', inputs[1])
    # Loop to go through all the races
    for i in range(len(times)):
        total_time = int(times[i])
        distance_required = int(distances[i])
        # You can get the distance travelled for each combination by multiplying the speed by the remaining time
        for time_charged in range(total_time):
            time_travelling = total_time - time_charged # For every ms not spend charging, the boat is moving
            distance_travelled = time_charged * time_travelling
            # If this is true, we have a winning combination and we can actually short circuit the rest of the calcs
            if distance_travelled > distance_required:
                total_unworkable_solutions = time_charged - 1
                # The unworkable solutions won't work on either end, so double it and append the rest to the total
                workable_solutions = total_time - (2 * total_unworkable_solutions) - 1 # Off by 1?
                total_solutions = total_solutions * workable_solutions
                break
    return total_solutions

if __name__ == "__main__":
    main()
