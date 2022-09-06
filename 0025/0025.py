with open('INPUT.txt', 'r') as inp:
    num1, num2 = int(inp.readline()), int(inp.readline())

with open('OUTPUT.txt', 'w') as out:
    if num1 == num2:
        out.write('=')
    elif num1 > num2:
        out.write('>')
    else:
        out.write('<')