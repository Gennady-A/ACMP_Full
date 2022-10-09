with open('INPUT.txt', 'r') as inp:
    num = int(inp.read().strip())

with open('OUTPUT.txt', 'w') as out:
    out.write(("12/09/" if (num%4==0 and num%100!=0) or num%400==0 else "13/09/") + "0"*(4-len(str(num))) + str(num)) 