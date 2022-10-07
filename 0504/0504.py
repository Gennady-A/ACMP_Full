start = "GCV"
with open('INPUT.txt', 'r') as inp:
    num = int(inp.read().strip())

with open('OUTPUT.txt', 'w') as out:
    for i in range(num):
        start = start[0] + start[2] + start[1]
        start = start[1] + start[0] + start[2]
    out.write(start)