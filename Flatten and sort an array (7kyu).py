def flatten_and_sort(array):
    flattened_list = []
    for x in array:
        for y in x:
            flattened_list.append(y)
    flattened_list.sort()
    return flattened_list
