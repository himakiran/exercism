def append(list1, list2):
    result = [None] * (len(list1)+len(list2))
    for i in range(0,len(list1)):
        result[i]=list1[i]
    for j,k in zip(range(len(list1),len(list2)+len(list1)),range(0,len(list2))):
        result[j]=list2[k]
    return result

def concat(lists):
    final_length = 0
    for each in lists:
        final_length += len(each)
    final_list=[None] * final_length
    counter = 0
    for each in lists:
        for i in range(0,len(each)):
            final_list[counter] = each[i]
            counter+=1 
    return final_list

def filter(function, list):
    result_list = [None] * len(list)
    result_list_counter = 0
    for each in list:
        if (function(each)):
            result_list[result_list_counter] = each
            result_list_counter+=1
    
    return result_list[0:result_list_counter]


def length(list):
    res_len = 0
    for each in list:
        res_len+=1
    return res_len


def map(function, list):
    l = len(list)
    result_list = [None] * l
    for i in range(0,l):
        result_list[i] = function(list[i])
    return result_list



def foldl(function, list, initial):
    if len(list)==0:
        return initial
    i = 0
    accumulator = function(initial,list[0])
    for i in range(1, len(list)):
        accumulator = function(accumulator,list[i])
    return accumulator



def foldr(function, list, initial):
    if len(list)==0:
        return initial
    i = 0
    l = len(list)
    accumulator = function(initial,list[l-1])
    for i in range(l-2,-1,-1):
        accumulator = function(accumulator,list[i])
    return accumulator


def reverse(list):
    l = len(list)
    rev_list = [None] * l
    for i,j in zip(range(l-1,-1,-1),range(0,l)):
        rev_list[j] = list[i]
    return rev_list
