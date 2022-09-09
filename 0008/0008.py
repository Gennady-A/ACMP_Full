with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write("YES" if (nums[0] * nums[1]) == nums[2] else "NO")