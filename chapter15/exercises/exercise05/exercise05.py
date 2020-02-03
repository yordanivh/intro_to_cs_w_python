def find_min_max(values: list):
    """Print the minimum and maximum value from values. """
    min = None
    max = None
    for value in values:
        if max is None or value > max:     
            max = value 
        if min is None or value < min:     
            min = value

print('The minimum value is {0}'.format(min)) 
print('The maximum value is {0}'.format(max))