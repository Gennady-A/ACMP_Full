with open('INPUT.txt', 'r') as inp:
    num = int(inp.read().strip())

with open('OUTPUT.txt', 'w') as out:
    out.write(str(sum([i for i in range(1, num+1) if num % i == 0])))