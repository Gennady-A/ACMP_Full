with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    nums = [int(i) for i in inp.readline().strip().split()]
    t = [str(i) for i in nums if i % 2 == 1]
    ch = [str(i) for i in nums if i % 2 == 0]

with open('OUTPUT.txt', 'w') as out:
    out.write(" ".join(t) + "\n" + " ".join(ch) + "\n" + ("YES" if len(ch) >= len(t)  else "NO"))