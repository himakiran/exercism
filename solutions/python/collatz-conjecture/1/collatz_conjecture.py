def do_even(num):
    return num/2

def do_odd(num):
    return (num*3)+1

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps=0
    while number!=1:
        if (number%2==0):
            number=do_even(number)
        else:
            number=do_odd(number)
        steps+=1
    return steps
