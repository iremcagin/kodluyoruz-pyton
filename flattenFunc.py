def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(input_list))
