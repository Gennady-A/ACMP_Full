with open('INPUT.txt', 'r') as inp:
    nums = inp.read().strip()

with open('OUTPUT.txt', 'w') as out:
    out.write("NO" if "0" in nums else "YES")