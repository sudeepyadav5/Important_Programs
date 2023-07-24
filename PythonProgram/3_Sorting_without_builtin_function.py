numbers = [9, 5, 2, 8, 1, 10]
print("Original List", numbers)

n = len(numbers)
swapped = True

while swapped:
    swapped = False
    for i in range(1, n):
        if numbers[i - 1] > numbers[i]:
            numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
            swapped = True
    
print("After Sorted list:", numbers)
