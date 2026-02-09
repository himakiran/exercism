import string
alph_str= string.ascii_lowercase
rev_str = ''.join(reversed(alph_str))
trans_table = str.maketrans(alph_str,rev_str)

def encode(plain_text):
    result = plain_text.lower().translate(trans_table).replace(" ","").translate(str.maketrans('', '', string.punctuation))
    result = ' '.join(result[i:i+5] for i in range(0,len(result),5))
    return result



def decode(ciphered_text):
    return ciphered_text.lower().translate(trans_table).replace(" ","")
