def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    max = data[0]
    count = 0
    for i in data:
        if max == i:
            print(max)
        count = data.count(max)
    return count
print(find_max_count([1,3,5,6,8,7,8,8]))
