with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(((nums[0] * nums[2] * 2) + (nums[1] * nums[2] * 2)) // 16 + (1 if ((nums[0] * nums[2] * 2) + (nums[1] * nums[2] * 2)) % 16 != 0 else 0)))