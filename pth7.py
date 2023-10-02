# Define an example array (list)
example_array = [5, 2, 9, 1, 5, 6]

# Sort the array in ascending order without using sorting functions
def custom_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sort the array in descending order without using sorting functions
def custom_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ascending Order
ascending_sorted_array = example_array.copy()
custom_sort_asc(ascending_sorted_array)
print("Ascending Order:", ascending_sorted_array)

# Descending Order
descending_sorted_array = example_array.copy()
custom_sort_desc(descending_sorted_array)
print("Descending Order:", descending_sorted_array)
