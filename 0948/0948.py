with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write((str(nums[1] // nums[0] + 1) if nums[1] % nums[0] != 0 else (str(nums[1] // nums[0]))) + " " + (str(nums[1] % nums[0]) if nums[1] % nums[0] != 0 else str(nums[0])))