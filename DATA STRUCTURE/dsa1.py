# Problem: Write a function that takes a list of integers and returns the maximum element.

def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# Example
numbers = [3, 7, 2, 9, 5]
print("Maximum:", find_max(numbers))
