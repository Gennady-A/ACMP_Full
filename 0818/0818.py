with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline().strip())
    nums = [int(i) for i in inp.readline().strip().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(sum(nums) - count + 1))