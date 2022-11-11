def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    min = data[0]
    odd = 0
    for i in data:
        if i > min:
            min = i
        if min % 2 != 0:
            odd = min
    return odd

