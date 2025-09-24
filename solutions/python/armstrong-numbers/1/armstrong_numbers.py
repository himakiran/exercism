def is_armstrong_number(number):
    num_of_digits=len(str(number))
    sum=0
    for each in str(number):
        sum+=int(each)**num_of_digits
    return number==sum
        
