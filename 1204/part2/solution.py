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
    total_scratchers = 0
    deserved_values = []
    seen_cards = 0
    for input in inputs:
        seen_cards += 1
        if len(deserved_values) < seen_cards:
            deserved_values.append(1)
        else:
            # Entering this conditional means that we have previous cards, just add to it
            deserved_values[seen_cards - 1] = deserved_values[seen_cards - 1] + 1

        # At this point we know how many scratchers of this card to add, so add it to the
        # total. After this that only goal is to potentially add scratchers for future tickets
        total_scratchers += deserved_values[seen_cards - 1]

        actual_values = input.split(':')
        split_nums = actual_values[1].split('|')
        winning_nums = re.findall(r'\d+', split_nums[0])
        ticket_nums = re.findall(r'\d+', split_nums[1])
        matching_nums = list(set(winning_nums).intersection(ticket_nums))
        for val in range(deserved_values[seen_cards - 1]):
            for iter in range(len(matching_nums)):
                if len(deserved_values) < seen_cards + (iter + 1):
                    deserved_values.append(1)
                else:
                    deserved_values[seen_cards + iter] = deserved_values[seen_cards + iter] + 1

    return total_scratchers
if __name__ == "__main__":
    main()
