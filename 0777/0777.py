with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(12 - nums[0]%12 + nums[1]) if nums[0]%12 > nums[1] else str(nums[1] - nums[0]%12))