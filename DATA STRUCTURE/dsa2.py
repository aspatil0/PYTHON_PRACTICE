# Problem: Write a function that reverses a list without using built-in reverse().

def reverse_list(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example
numbers = [1, 2, 3, 4, 5]
print("Reversed:", reverse_list(numbers))
