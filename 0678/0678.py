l = [1, 0, 0]

with open('INPUT.txt', 'r') as inp:
    commands = list(inp.read().strip())

for i in commands:
    if i == "A":
        l[0], l[1] = l[1], l[0]
    if i == "B":
        l[2], l[1] = l[1], l[2]
    if i == "C":
        l[0], l[2] = l[2], l[0]

with open('OUTPUT.txt', 'w') as out:
    out.write(str(l.index(1)+1))