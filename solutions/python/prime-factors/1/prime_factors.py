def factors(value):
    factor_list = []
    i=2
    while( value > 1 ):
        if value % i == 0:
            factor_list.append(i)
            value = value // i
        else:
            i+=1
    return factor_list
    
    
