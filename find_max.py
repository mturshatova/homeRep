def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Test the function
test_array = [3, 7, 2, 9, 1]
print("Maximum value in the array:", find_max(test_array))

