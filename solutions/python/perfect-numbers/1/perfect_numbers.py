def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        sum_of_factors = sum(find_factors(number))
        result=""
        if sum_of_factors == number:
            result+="perfect"
        if number < sum_of_factors:
            result+="abundant"
        if number > sum_of_factors:
            result+="deficient"
        return result
            
            

def find_factors(number):
    """ Returns a list of factors of a positive integer.

    :param number: int a positive integer
    :return: list of integers which are factors of the number
    """
    factors_list=[]
    for each in range(1,number):
        if number%each==0:
            factors_list.append(each)
    return factors_list
    