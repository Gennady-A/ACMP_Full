with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str( (nums[1] * (nums[2] - 1)  - 1) + (nums[3] if nums[2] % 2 != 0 else nums[1] - nums[3] + 1) ))