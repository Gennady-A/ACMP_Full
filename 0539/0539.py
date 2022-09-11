with open("INPUT.txt", "r") as inp:
    num = int(inp.read())

with open("OUTPUT.txt", "w") as out:
    if num == 1:
        out.write("0")
    else:
        out.write(str(int(num/2)) if num%2 == 0 else str(num))
