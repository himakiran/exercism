def is_paired(input_string):
    start_brackets = ['[','{','(']
    end_brackets = [']','}',')']
    #return True if empty string 
    if input_string=='':
        return True
    #return False if string length is one and the character is either in start_brackets or end_brackets
    if len(input_string)==1 and (input_string in start_brackets or input_string in end_brackets):
        return False
    # else return True
    if len(input_string)==1 and not (input_string in start_brackets or input_string in end_brackets):
        return True
    # we traverse the string from left to right. anytime we find a character in start_brackets we add it to a list-tracker
    # and update latest_start variable to that char. If we find a end_bracket character, then we check if it is the exact
    # same closing character. If True we pop the character from the tracker and update the latest_start variable to the previous variable in
    # the tracker list. If we find a end_bracket character and it is not 
    # not the same closing character, the program ends and return False. If it is any other character the program continues.
    # after all the characters have been parsed. we check the status of tracker. If it is empty then True, else False
    tracker_list = []
    latest_start = ''
    for each in input_string:
        if each in start_brackets:
            tracker_list.append(each)
            latest_start = each
        if each in end_brackets:
            if (each==']' and latest_start=='[') or (each=='}' and latest_start=='{') or (each==')' and latest_start=='('):
                if len(tracker_list)>=1:
                    tracker_list.pop()
                    if len(tracker_list)>=1:
                        latest_start=tracker_list[-1]
                    else:
                        latest_start=''
            elif (each==']' and not latest_start=='[') or (each=='}' and not latest_start=='{') or (each==')' and not latest_start=='('):
                return False
    if len(tracker_list) >= 1:
        return False
    else:
        return True
