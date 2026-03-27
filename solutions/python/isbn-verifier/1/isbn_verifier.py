def is_valid(isbn):
    isbn_digits =[]
    for each in isbn[:-1]:
        if not (each.isdigit() or each=="-"):
            return False
        if each.isdigit():
            isbn_digits.append(int(each))
        if len(isbn_digits) > 9:
            return False
    if len(isbn_digits) < 9:
        return False
    if not (isbn[-1].isdigit() or isbn[-1]=="X"):
        return False
    if isbn[-1].isdigit():
        isbn_digits.append(int(isbn[-1]))
    if isbn[-1]=="X":
        isbn_digits.append(10)
    
    sum_isbn_digits = isbn_digits[0] * 10 + isbn_digits[1] * 9 + isbn_digits[2] * 8 + isbn_digits[3] * 7 + isbn_digits[4] * 6 + isbn_digits[5] * 5 + isbn_digits[6] * 4 + isbn_digits[7] * 3 + isbn_digits[8] * 2 + isbn_digits[9] * 1
    return (sum_isbn_digits%11==0)