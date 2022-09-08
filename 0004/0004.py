with open("INPUT.txt", "r") as inp:
    num = int(inp.read())

with open("OUTPUT.txt", "w") as out:
    out.write(str(num) + "9" + str(9-num))