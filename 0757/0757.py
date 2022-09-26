with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(min([nums[0]//2, nums[1]//6, nums[2]])))