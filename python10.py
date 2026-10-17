
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

nums = [12, 45, 7, 89, 45, 67]
print("Second Largest:", second_largest(nums))