import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user, until a valid `int` is entered.
    :param prompt: The String the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("'{0}' is not a valid number".format(temp))

# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)
help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 # initialize number that doesn't equal answer

while guess != answer:
    guess = get_integer("-> ")
    if guess == answer:
        print("Well done. You guessed the number!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: # guess must be higher than answer
            print("Please guess lower")
