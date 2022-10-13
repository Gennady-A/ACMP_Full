with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    nums = [int(i) for i in inp.readline().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(min(nums)) + " " + str(max(nums)))