with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    nums = inp.readline().split()

with open('OUTPUT.txt', 'w') as out:
    out.write(str(" ".join(nums[::-1])))