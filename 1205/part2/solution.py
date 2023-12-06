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
    # First, we need to get the list of initial seeds to send through the transformations
    seed_numbers = []
    outputs = []
    # If an input line contains the word map, it means we've moved on to the next transformation
    map_text = "map"
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    # This is the list of transformations we will eventually send each of the seeds through
    list_of_transformations = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    
    # Corresponds to which transformation we are currently adding to
    transformation_index = -1
    for index, input in enumerate(inputs, start=0):
        if index == 0:
            seed_numbers = re.findall(r'\d+', input)
            # Skip whitespace
        elif bool(re.match(r'^\s*$', input)):
            continue
        elif map_text in input:
            transformation_index += 1
        # If we hit this conditional, that means we've hit a new transformation index
        else:
            # If we get to this point, then we are within a transformation and we just need to add to it
            conversion_nums = re.findall(r'\d+', input)
            # Add to the dictionary a tuple of the lower and upper bound as well as the offset value
            list_of_transformations[transformation_index].append((int(conversion_nums[0]), int(conversion_nums[1]), int(conversion_nums[2])))
    # Outside of the for loop, we have set up all the transformation values and now we just have to loop through them
    # and get the output value for each seed.

    # instead of looping through all the values, what we should do is look at the range which outputs the lowest possible values in each
    # transformation and go backwards from there. This will result in values to consider at layer 6, then repeat for layer 5, layer 4, etc
    # All the way to seed ranges which will result in the lowest possible values. If any of the available seeds fall into these ranges, consider
    # These when looking for the lowest seed.
    for  i in range(0, len(seed_numbers), 2):
        initial_value = int(seed_numbers[i])
        end_value = initial_value + int(seed_numbers[i+1])
        for j in range(initial_value, end_value):
            print("NEW SEED")
            current_value = j
            # Loop through the transformations
            for transformation in list_of_transformations:
                for val_range in transformation:
                    if current_value >= val_range[1] and current_value <= (val_range[1] + val_range[2]):
                        # If we're between the values, set it equal to the value + the offset
                        print("Changing from " + str(current_value) + " to " + str(current_value + (val_range[0] - val_range[1])))
                        current_value = current_value + (val_range[0] - val_range[1])
                        break
            outputs.append(current_value)
    return min(outputs)

if __name__ == "__main__":
    main()
