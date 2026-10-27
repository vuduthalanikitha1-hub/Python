def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

numbers = [1, 2, 3, 4, 5]
print(rotate_right(numbers, 2))