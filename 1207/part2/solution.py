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
    bet_total = 0
    # Hands will be a list of triples, with the first entry being what kind of hand
    # it is, the second being the hand itself, and 3rd the bet. Hands are stored as the following:
    # 1: Five of a kind
    # 2. Four of a kind
    # 3. Full House
    # 4. Three of a kind
    # 5. Two pair
    # 6. One pair
    # 7. High card
    hands = []
    # First, we need to parse the input and track what type of hand each one is
    for input in inputs:
        tokens = input.split()
        hand = tokens[0]
        bet = tokens[1]
        # First figure out what kind of hand it is
        hand_type = get_hand_type(hand)
        hands.append((hand_type, hand, bet))
    # Now that we have a list of hands and bets, order them based on first their 
    # Hand strength followed by their respective ordered cards
    ordered_hands = sorted(hands, key = get_hand_strength)
    for index, hand in enumerate(ordered_hands):
        bet_total += (index + 1) * int(hand[2])

    return bet_total

def get_hand_strength(hand):
    hand_map = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    cards = list(hand[1])
    return (hand[0], hand_map.get(cards[0]), hand_map.get(cards[1]), hand_map.get(cards[2]), hand_map.get(cards[3]), hand_map.get(cards[4]))

def get_hand_type(hand):
    cards_seen = {}
    # The max of any card seen
    max_seen = (1, "2")
    second_max_seen = (1, "2")
    for card in hand:
        if card in cards_seen:
            new_value = cards_seen[card] + 1
            cards_seen[card] = new_value
            if new_value > max_seen[0] and card != "J":
                max_seen = (new_value, card)
            elif new_value > second_max_seen[0] and card != "J":
                second_max_seen = (new_value, card)
            else:
                # No op
                continue

        else:
            cards_seen[card] = 1
    # Now we should be able to tell what kind of hand it is based on
    # The most seen and second most seen card values
    if "J" in cards_seen:
        j_seen = cards_seen["J"]
        max_seen = (min(5, max_seen[0] + j_seen), max_seen[1])

    # KTJJT is being seen as a full house instead of 4 of a kind
    if max_seen[0] == 5:
        return 7 # Five of a kind
    elif max_seen[0] == 4:
        return 6 # Four of a kind
    elif max_seen[0] == 3 and second_max_seen[0] == 2:
        return 5 # Full house
    elif max_seen[0] == 3:
        return 4 # Three of a kind
    elif max_seen[0] == 2 and second_max_seen[0] == 2:
        return 3 # Two pair
    elif max_seen[0] == 2:
        return 2 # One pair
    else:
        return 1 # High card

if __name__ == "__main__":
    main()
