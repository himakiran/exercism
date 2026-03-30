import string
def is_pangram(sentence):
    alphabets = list(string.ascii_lowercase)
    sentence_lc = sentence.lower()
    for each in sentence_lc:
        if each in alphabets:
            alphabets.remove(each)
    return not alphabets
    
    
