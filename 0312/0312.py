with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str((nums[1] - nums[0]) * (nums[2] - 1) + nums[0]))