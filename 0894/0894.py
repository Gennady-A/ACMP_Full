import math

with open('INPUT.txt', 'r') as inp:
    nums = [float(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str( round((((math.pi * nums[1]**2)-nums[0]) / math.pi)**(0.5), 3) ))