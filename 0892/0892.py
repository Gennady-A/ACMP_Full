with open('INPUT.txt', 'r') as inp:
    num = int(inp.read())

with open('OUTPUT.txt', 'w') as out:
    if num > 12 or num < 1:
        out.write("Error")
    elif num >= 3 and num <= 5:
        out.write("Spring")
    elif num >= 6 and num <= 8:
        out.write("Summer")
    elif num >= 9 and num <= 11:
        out.write("Autumn")
    else:
        out.write("Winter")