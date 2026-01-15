""" This function implements binary search to find square root of a number"""
def square_root(number):
    square_root = 1
    while((square_root*square_root)!=number):
        if((square_root*square_root)>number):
            square_root -=1
        elif((square_root*square_root)<number):
            square_root+=1
    return square_root
            

    
