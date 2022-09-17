with open('INPUT.txt', 'r') as inp:
    num = inp.read().strip()

with open('OUTPUT.txt', 'w') as out:
    out.write("25" if len(num) == 1 else str(int(num[:-1])*(int(num[:-1])+1))+"25")