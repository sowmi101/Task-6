
def find_middle_value(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Calculate the middle index
    middle_index = len(arr) // 2
    
    if len(arr) % 2 == 1:
        # Odd number of elements
        middle_value = arr[middle_index]
    else:
        # Even number of elements, take the average of two middle values
        middle_value = (arr[middle_index - 1] + arr[middle_index]) / 2.0
    
    return middle_value

arr = [2,6,4,1,8,9]
print("Middle Value:",find_middle_value(arr))