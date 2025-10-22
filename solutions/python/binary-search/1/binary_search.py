def find(search_list, value):
    length_list = len(search_list)
    start=0
    end=length_list-1
    found=-1
    
    while end >= start:
        middle = int(end-start/2)
        middle_item = search_list[middle]
        if middle_item==value:
            found=middle
            break
        elif middle_item > value:
            end=middle-1
        else:
            start=middle+1
    if found==-1:
        raise ValueError("value not in array")
    else:
        return found 
