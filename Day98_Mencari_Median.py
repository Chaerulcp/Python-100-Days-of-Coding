def find_median(numbers):
    n = len(numbers)
    numbers.sort()

    if n % 2 == 0:
        median1 = numbers[n//2]
        median2 = numbers[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = numbers[n//2]

    return median

# hasil function
print(find_median([1, 2, 3, 4, 5])) # output: 3
print(find_median([1, 2, 3, 4, 5, 6])) # output: 3.5
