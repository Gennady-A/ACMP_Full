def gbc(fn, sn):
    return gbc(sn, fn % sn) if sn else fn

def main():
    with open('INPUT.txt', 'r') as inp:
        n = int(inp.read())

    ans = 0

    for i in range(1, n):
        ans += 1 if gbc(i, n) == 1 else 0

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(ans))

if __name__ == '__main__':
    main()
