def color_code(color):
    resistor_dict={'black':0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
    return resistor_dict[color]


def colors():
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]

def value(colors):
    result=''
    result+=str(color_code(colors[0]))
    result+=str(color_code(colors[1]))
    result=int(result)
    return result
