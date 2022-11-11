def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    max = data[0]
    even = 0
    for i in data:
        if i > max:
            max = i
        
        if max % 2 == 0:
            even = max
    return even
print(find_max_even([1, 2, -3, 4, 5]))