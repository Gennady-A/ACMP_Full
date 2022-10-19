def count_of_queen(n):
    if n == 1 or n == 2:
        return 0
    else:
        return 2*(n-2) + count_of_queen(n-1)

with open('INPUT.txt', 'r') as inp:
    num = int(inp.readline())

with open('OUTPUT.txt', 'w') as out:
    out.write(str(count_of_queen(num)))