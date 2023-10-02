# Define an example array (list)
example_array = [5, 2, 9, 1, 5, 6, 8, 3]

# Calculate the length of the array
array_length = len(example_array)

# Check if the array has an odd or even number of elements
if array_length % 2 == 0:
    # If the array has an even number of elements, split it into two equal halves
    middle_index = array_length // 2
    first_half = example_array[:middle_index]
    second_half = example_array[middle_index:]
else:
    # If the array has an odd number of elements, the first half has one less element
    middle_index = array_length // 2
    first_half = example_array[:middle_index]
    second_half = example_array[middle_index + 1:]

# Calculate the sum of elements in each half
sum_first_half = sum(first_half)
sum_second_half = sum(second_half)

# Calculate the weightage (sum) of the first half and second half
print("Weightage of First Half:", sum_first_half)
print("Weightage of Second Half:", sum_second_half)
