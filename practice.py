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
# Take an array of integers (positive or negative or both) and
# return the sum of the absolute value of each element.


def get_abs_sum(nums):
    sum = 0
    for i in nums:
        sum += abs(i)
    return sum


print(get_abs_sum(test_list))


# https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
# Create a function that takes a string  and returns a string
# with its letters in alphabetical order.


def alphabet_soup(text):
    text = list(text)
    text.sort()
    return ''.join(text)


print(alphabet_soup('python'))


# https://edabit.com/challenge/GrPXERNbrjyCmHPDg
# Create a function that takes a string and returns the number of
# alphanumeric characters that occur more than once.


def duplicate_count(txt):
    dup_chars = 0
    my_set = set(txt)
    for i in my_set:
        count = 0
        for j in txt:
            if i == j:
                count += 1
        if count > 1:
            dup_chars += 1
    return dup_chars


print(duplicate_count('Indivisibilities'))  # should be 2


# https://edabit.com/challenge/bPHcgMpkf9WvbwbAo
# Create a function that accepts an array of 10 integers (between 0 and 9)
# and returns a string of those numbers in the form of a phone number.


def format_phone_number(num):
    n = '(%s%s%s) %s%s%s-%s%s%s%s'
    phone = list(str(num))
    return n % tuple(phone)


print(format_phone_number(1234567890))


# https://edabit.com/challenge/97Shytt5nzjX4YWzJ
# Write a function that takes a string of brackets and checks whether
# they are balanced or not.


def is_balanced(str):
    if len(str) > 0:
        bracket_reference = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for character in str:
            if character in bracket_reference.keys():
                stack.append(character)
            elif character in bracket_reference.values():
                if bracket_reference[stack[-1]] == character:
                    stack.pop()
                else:
                    return False
        return not len(stack)
    else:
        return 'none'


print(is_balanced('{{[[(())[]]]}}'))

