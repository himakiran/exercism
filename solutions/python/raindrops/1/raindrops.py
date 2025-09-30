def convert(number):
    result=""
    divisible=False
    if number%3==0:
        divisible=True
        result+="Pling"
    if number%5==0:
        divisible=True
        result+="Plang"
    if number%7==0:
        divisible=True
        result+="Plong"
    if not divisible:
        result+=str(number)
    return result
