with open('INPUT.txt', 'r') as inp:
    num = inp.read().strip()
with open('OUTPUT.txt', 'w') as out:
    out.write(str("YES" if num[:2] == num[-1:1:-1] else "NO"))