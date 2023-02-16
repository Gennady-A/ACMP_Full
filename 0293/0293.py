def main():
    with open('INPUT.txt', 'r') as inp:
        n = int(inp.readline())
        m = [int(i) for i in inp.readline().strip().split()]
        p = [int(i) for i in inp.readline().strip().split()]

    d = [(m[i]*p[i]/100) for i in range(len(m))]
    ans = str(d.index(max(d)) + 1)

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()