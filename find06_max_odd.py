def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    max = data[0]
    max = 0
    for i in data:
        if i > max:
            max = i
        if max % 2 != 0:
            odd = max
    return odd