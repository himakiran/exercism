def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number==1:
        return 1
    else:
        return 2*square(number-1)


def total():
    total=0
    for num in range(1,65):
        total+=square(num)
    return total
