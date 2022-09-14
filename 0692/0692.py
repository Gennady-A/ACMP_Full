with open('INPUT.txt', 'r') as inp:
    num = int(inp.read())

with open('OUTPUT.txt', 'w') as out:
    if str(bin(num)).count("1") == 1 and num > 0:
        out.write("YES")
    else:
        out.write("NO")