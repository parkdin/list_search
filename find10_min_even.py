def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    min = data[0]
    even = 0
    for i in data:
        if i < min:
            min = i
        if min % 2 == 0:
            even = min
    return even

