def square_of_sum(number):
    sum=0
    for each in range(0,number+1):
        sum+=each
    return sum*sum


def sum_of_squares(number):
    sum=0
    for each in range(0,number+1):
        sum+=(each*each)
    return sum


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
