# Chandler Supple, 5/17/2018
# Call with the function - standard_deviation(dataset)

import math

def standard_deviation(input_x):
    x = input_x.split(',')
    x = list(map(int, x))
    n = (len(x))
    x_bar = 0
    numerator = 0
    for num in range (0, n):
        x_bar = x_bar + x[num]
    x_bar = x_bar / (n)
    for num in range (0, n):
        numerator = numerator + ((x[num] - x_bar)**2)
    sd_under_root = numerator / (n)
    sd = math.sqrt(sd_under_root)
    print('Dataset Given: %s' %(x))
    print('Standard Deviation: %s' %(sd))
