import string
alph_str = string.ascii_letters
kata_len = {}
count=1
for each in range(0,26):
    kata_len[alph_str[each]]=count
    count+=2


def calculate_length_of_kata(letter):
    letter = letter.lower()
    return kata_len[letter]

def middle_string(letter):
    num_of_spaces = calculate_length_of_kata(letter)-2
    return letter + " "*num_of_spaces + letter

def top_triangle(len_of_middle=0,letter='A'):
    letters = alph_str[:alph_str.index(letter.lower())]
    num_spaces_either_side = int((len_of_middle-1)/2)
    num_spaces_middle = 1
    triangle_list = []
    triangle_list.append(" "*num_spaces_either_side+'A'+" "*num_spaces_either_side)
    for each in letters[1:]:
        each = each.upper()
        num_spaces_either_side-=1
        triangle_list.append(" "*num_spaces_either_side+each+" "*num_spaces_middle+each+" "*num_spaces_either_side)
        num_spaces_middle+=2
    return triangle_list

def draw_kata(triangle_list,letter):
    result = []
    if letter == 'A':
        result.append("A")
    else:
        for each in triangle_list:
            result.append(each)
        result.append(middle_string(letter))
        for each in triangle_list[::-1]:
            result.append(each)
    return result

def rows(letter):
    #print(calculate_length_of_kata(letter))
    return draw_kata(top_triangle(calculate_length_of_kata(letter),letter),letter)





    


