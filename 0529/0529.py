with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str((abs(nums[0] - nums[2])**2 + abs(nums[1] - nums[3])**2)**0.5))