with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str( min([nums[0], nums[3]]) * nums[1] + ((nums[3] - nums[0]) * nums[2] if nums[3] > nums[0] else 0) ))