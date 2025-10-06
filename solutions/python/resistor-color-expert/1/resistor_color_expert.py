def color_code(color):
    resistor_dict={'black':0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
    return resistor_dict[color]

def tolerance(color):
    tolerance_dict={"grey":0.05,"violet":0.1,"blue":0.25,"green":0.5,"brown":1,"red":2,"gold":5,"silver":10}
    return "±"+str(tolerance_dict[color])+"%"



def value(colors):
    result=''
    for each in colors:
        result+=str(color_code(each))
    #result=int(result)
    return result

def append_zeroes(rvalue,zeros):
    rvalue=rvalue+zeros
    rvalue=int(rvalue)
    if rvalue < 999:
        result=str(rvalue)+" ohms"
    if rvalue > 999 and rvalue < 1000000:
        result=int(rvalue/1000) if ((rvalue % 1000) ==0 ) else rvalue/1000
        result=str(result)+" kiloohms"
    if rvalue >= 1000000 and rvalue < 1000000000:
        result=int(rvalue/1000000) if ((rvalue % 1000000) ==0 ) else rvalue/1000000
        result=str(result)+" megaohms"
    if rvalue >= 1000000000:
        result=int(rvalue/1000000000) if ((rvalue % 1000000000) ==0 ) else rvalue/1000000
        result=str(result)+" gigaohms"
        
    if int(rvalue)==0:
        return '0 ohms'
    result=result.lstrip('0')
    return result

def label(colors):
    if len(colors)==1:
        result=str(color_code(colors[0]))+" ohms"
    if len(colors)>=3:
        result=''
        kilo=False
        mega=False
        giga=False
        if len(colors)==3:
            result+=value(colors[:2])
            zeros ='0'*color_code(colors[2])
            result=append_zeroes(result,zeros)
        if len(colors)==4:
            result+=value(colors[:2])
            zeros ='0'*color_code(colors[2])
            result=append_zeroes(result,zeros)
            result=result+" "+tolerance(colors[3])
        if len(colors)==5:
            result+=value(colors[:3])
            zeros ='0'*color_code(colors[3])
            result=append_zeroes(result,zeros)
            result=result+" "+tolerance(colors[4])
    return result

def resistor_label(colors):
    return label(colors)