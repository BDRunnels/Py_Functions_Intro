def multiply(a: float, b: float) -> float:
    """
    Will take 2 arguments `a` & `b` and multiply them.
    :param a: first `int`
    :param b: second `int`
    :return: `int` of `a` * `b`
    """
    return a * b


def is_palindrome(string: str) -> bool:
    return string.casefold() == string[::-1].casefold()

# MY ANSWER
def is_palindrome_sentence(string: str) -> bool:
    answer_string = ""
    for char in string.casefold():
        if 'a' <= char <= 'z':
            answer_string += char

    return is_palindrome(answer_string)

# HIS ANSWER
def is_p_sentence(string):
    string = ""
    for char in string:
        if char.isalnum():
            string += char

    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number for positive `n`"""
    if 0 <= n <= 1:
        return n
    n_minus_1, n_minus_2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = is_palindrome_sentence()
# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)


# word = input("Please enter a word to check for palindrome: ")
# if is_palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is NOT a palindrome".format(word))
answer = multiply(18, 3)
print(answer)

######
# Palindrome Sentences
p1 = "Was it a car, or a cat, I saw?"
p2 = "Do geese see god?"
p3 = "Desnes not far, Rafton sensed."
