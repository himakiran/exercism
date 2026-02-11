def count_ones(decimalnumber):
    quotient = decimalnumber
    count=0
    while(quotient>0):
        remainder = quotient % 2
        if remainder==1:
            count+=1
        quotient = quotient // 2
    return count
        

def egg_count(display_value):
    return count_ones(display_value)
