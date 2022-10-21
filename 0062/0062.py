letters = list("ABCDEFGH")

with open('INPUT.txt', 'r') as inp:
    pos = list(str(inp.read()))

with open('OUTPUT.txt', 'w') as out:
    out.write("BLACK" if (letters.index(pos[0]) + 1 + int(pos[1])) % 2 == 0 else "WHITE")