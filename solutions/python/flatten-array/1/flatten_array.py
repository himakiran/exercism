def flatten(iterable):
    flat_list = []
    for each in iterable:
        try:
            flat_list.extend(flatten(each))
        except:
            if each!=None:
                flat_list.append(each)
    return flat_list
