with open('INPUT.txt', 'r') as inp:
    nums = list(map(int, list(inp.readline().strip())))

with open('OUTPUT.txt', 'w') as out:
    out.write("YES" if sum(nums[:3]) == sum(nums[3:]) else "NO")