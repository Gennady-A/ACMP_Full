with open("INPUT.txt", "r") as inp:
    num = int(inp.read())
with open("OUTPUT.txt", "w") as out:
    out.write(str(int(num/6))+" "+str(int(num/6*4))+" "+str(int(num/6)))
