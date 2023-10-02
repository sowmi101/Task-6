# Define an example array (list)
example_array = [5, 2, 9, 1, 5, 6]

# Iterate through the elements at even indices and print them
for index, value in enumerate(example_array):
    if index % 2 == 0:
        print("Value at even index", index, ":", value)
