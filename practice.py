# https://edabit.com/challenge/A7hyDnb72prWryeuY
# find the largest number in a list

test_list = [3, -5, 7, 8, 2, -45, 7, -4, 8]


def return_largest(nums):
    mem = 0
    for i in nums:
        if i > mem:
            mem = i
    return mem


print(return_largest(test_list))


# https://edabit.com/challenge/rCmEy2AQYLbRGgKyL
# Take an array of integers (positive or negative or both) and return the sum of the absolute value of each element.


def get_abs_sum(nums):
    sum = 0
    for i in nums:
        sum += abs(i)
    return sum


print(get_abs_sum(test_list))


# https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
# Create a function that takes a string  and returns a string with its letters in alphabetical order.


def alphabet_soup(text):
    text = list(text)
    text.sort()
    return ''.join(text)


print(alphabet_soup('python'))
