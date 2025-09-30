def is_isogram(string):
    letters_list=[]
    for each in string:
        if each.isalpha():
            if each.lower() not in letters_list:
                letters_list.append(each.lower())
            else:
                return False

    return True
            
