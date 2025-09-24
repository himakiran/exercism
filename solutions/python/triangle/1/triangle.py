def isTriangle(sides):
    if not (sides[0] >0 and sides[1] >0 and sides[2] > 0):
        return False
    if not (sides[0]+sides[1]>= sides[2] and sides[1]+sides[2]>=sides[0] and sides[0]+sides[2]>=sides[1]):
        return False
    return True


def equilateral(sides):
    if isTriangle(sides) and sides[0]==sides[1] and sides[1]==sides[2]:
        return True
    return False
    

def isosceles(sides):
    if isTriangle(sides) and ((sides[0]==sides[1]) or (sides[1]==sides[2]) or (sides[0]==sides[2])):
        return True
    return False


def scalene(sides):
    if isTriangle(sides) and (sides[0]!=sides[1] and sides[1]!=sides[2] and sides[2]!=sides[0]):
        return True
    return False
