with open('INPUT.txt', 'r') as inp:
    nums = int(inp.read())

with open('OUTPUT.txt', 'w') as out:
    out.write(str(nums + 1))