import string
alph_str= string.ascii_lowercase
rev_str = alph_str[::-1]
num_str = string.digits

def encode(plain_text):
    result = ""
    count = 0
    plain_text=plain_text.lower()
    for each in plain_text:
        if each in alph_str:
            res=rev_str[alph_str.index(each)]
            count+=1
        elif each in num_str:
            res=each
            count+=1
        else:
            res=""
        result+=res
        
        if(count==5):
            count=0
            result+=" "
    return result.rstrip(" ")


def decode(ciphered_text):
    result = ""
    for each in ciphered_text:
        if each in rev_str:
            res=alph_str[rev_str.index(each)]
        elif each==" ":
            res=""
        else:
            res=each
        result+=res
    return result
