import math
def score(x, y):
    radius_xy=math.sqrt((x*x)+(y*y))
    result=0
    if radius_xy>10:
        return result
    if (radius_xy<=10) and (radius_xy>5):
        result=1
    if (radius_xy<=5) and (radius_xy>1):
        result=5
    if (radius_xy<=1) and (radius_xy>=0):
        result=10
    return result
    
