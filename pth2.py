def find_max_and_min(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return None;

    # Initialize max and min with the first element of the array
    max_value = arr[0]
    min_value = arr[0]

    # Iterate through the array to find the max and min values
    for element in arr:
        if element > max_value:
            max_value = element
        elif element < min_value:
            min_value = element

    return max_value, min_value

example_array = [5, 2, 9, 1, 5, 6]

max_val, min_val = find_max_and_min(example_array)
print("Maximum Value:", max_val)
print("Minimum Value:", min_val)
