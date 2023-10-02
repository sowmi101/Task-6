# Define an example array (list)
example_array = [5, 2, 9, 1, 5, 6]

# Iterate through the elements at odd indices and print them
for index, value in enumerate(example_array):
    if index % 2 == 1:
        print("Value at odd index", index, ":", value)
