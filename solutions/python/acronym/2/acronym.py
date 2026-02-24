import string

def abbreviate(words):
    """
    returns abbreviation of string
    """
    punct_string = ''.join(x for x in string.punctuation if x!="-")
    words = ''.join(e for e in words if e not in punct_string)
    wlist = words.split(" ")
    rlist = []
    for each in wlist:
        if "-" in each:
            each_list = each.split("-")
            for each1 in each_list:
                rlist.append(each1)
        else:
            rlist.append(each)
    abbrvn=""
    for each in rlist:
        if each!="":
            abbrvn+=each[0].upper()
    return abbrvn
    
