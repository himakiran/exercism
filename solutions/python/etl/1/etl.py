def transform(legacy_data):
    result_dict = {}
    for key, value in legacy_data.items():
        for each in value:
            result_dict[each.lower()] = key
    return result_dict
        
