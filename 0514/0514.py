with open('INPUT.txt', 'r') as inp:
    count = int(inp.read().strip())

with open('OUTPUT.txt', 'w') as out:
    i = [0]
    while sum(i) + i[-1] + 1 <= count:
        i.append(i[-1] + 1)
        print(i)
    out.write(str(len(i)-1))