def commands(binary_str):
    secret_dict ={1:'wink',2:'double blink',4:'close your eyes',8:'jump',16:'reverse'}
    result=[]
    input_int=int(binary_str,2)
    if input_int & 1:
        result.append(secret_dict[1])
    if input_int & 2:
        result.append(secret_dict[2])
    if input_int & 4:
        result.append(secret_dict[4])
    if input_int & 8:
        result.append(secret_dict[8])
    if input_int & 16:
        result_list = result[::-1]
        result = result_list
    return result 
