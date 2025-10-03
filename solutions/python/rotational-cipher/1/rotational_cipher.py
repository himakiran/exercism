import string
def rotate(text,key):
    alphabets_list = list(string.ascii_lowercase)
    result=[]
    UPPER=False
    for each in text:
        if each.isalpha():
            if each.isupper():
                each=each.lower()
                UPPER=True
            position=alphabets_list.index(each)
            if (position+key) > 25:
                position=(position+key)%26
            else:
                position+=key
                
            if UPPER:
                result.append(alphabets_list[position].upper())
            else:
                result.append(alphabets_list[position])
            UPPER=False
        else:
            result.append(each)
    return "".join(result)
    
    

