def main():
    with open('INPUT.txt', 'r') as inp:
        n, m = [int(i) for i in inp.readline().strip().split()]
        racersName = []
        racersResult = []

        for i in range(n):
            racersName.append(inp.readline())
            racersResult.append(sum([int(i) for i in inp.readline().strip().split()]))

    with open('OUTPUT.txt', 'w') as out:
        out.write(racersName[racersResult.index(min(racersResult))])

if __name__ == '__main__':
    main()