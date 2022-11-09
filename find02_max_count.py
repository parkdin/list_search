def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    max = data[0]
    for i in data:
        if i > max:
            max = i 
        k = data.count(max)
    return k
print(find_max_count([1,3,5,6,8,7,8,8]))
