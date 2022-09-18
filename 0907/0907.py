with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write("YES" if nums[2]*2 <= nums[1] and nums[2]*2 <= nums[0] else "NO")