numbers = (0,1,2,3,4,5)

# print(numbers, sep=";")
# print(*numbers, sep=";") # * unpacks the tuple


def test_star(*args): # replaced with an unpacked tuple
    print(args)
    for x in args:
        print(x)


test_star(0,1,2,3,4,5)

print()
test_star()
