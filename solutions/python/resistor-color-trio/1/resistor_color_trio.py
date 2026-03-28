def color_code(color):
    resistor_dict={'black':0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
    return resistor_dict[color]

def value(colors):
    result=''
    result+=str(color_code(colors[0]))
    result+=str(color_code(colors[1]))
    #result=int(result)
    return result

def count_zeroes(result):
    count=0
    for each in result:
        if each=='0':
            count+=1
    return count

def append_suffix(result,suffix):
    if suffix=='kilo':
        result=''.join(list(result)[:-3])
        result+=' kiloohms'
    if suffix=='mega':
        result=''.join(list(result)[:-6])
        result+=' megaohms'
    if suffix=='giga':
        result=''.join(list(result)[:-9])
        result+=' gigaohms'
    return result
def label(colors):
    result=''
    result+=value(colors[:2])
    kilo=False
    mega=False
    giga=False
    zeros ='0'*color_code(colors[2])
    result+=zeros
    if count_zeroes(result) >= 9:
        return append_suffix(result,'giga')
    if count_zeroes(result) >= 6:
        return append_suffix(result,'mega')
    if count_zeroes(result) >= 3:
        return append_suffix(result,'kilo')
    if int(result)==0:
        return '0 ohms'
    result+=' ohms'
    
    return result.lstrip('0')
