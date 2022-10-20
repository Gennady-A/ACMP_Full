with open('INPUT.txt', 'r') as inp:
    num = int(inp.readline().strip())

with open('OUTPUT.txt', 'w') as out:
    out.write(str(((3+4-num%6) if num%6 != 0 else 0) + 1*num//6 ) + " " + str(num * 6))