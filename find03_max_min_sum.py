def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    min = data[0]
    max = data[0]
    for i in data:
        if i > max:
            max = i
    for j in data:
        if j < min:
            min = j
    sum = max + min
    return sum