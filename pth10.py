# Define an example array (list)
example_array = [5, 2, 9, 1, 7, 6, 11, 13]

# Define the value to search for
target_value = 40

# Initialize a variable to store the index where the value is found
found_index = None

# Iterate through the array to search for the target value
for index, value in enumerate(example_array):
    if value == target_value:
        found_index = index
        break

# Check if the value was found and print the result
if found_index is not None:
    print(f"The value {target_value} was found at index {found_index}.")
else:
    print(f"The value {target_value} was not found in the array.")
