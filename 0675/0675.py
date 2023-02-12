def main():
    with open('INPUT.txt', 'r') as inp:
        n, m = [int(i) for i in inp.readline().strip().split()]

        nXmMatrix = []

        for i in range(n):
            nXmMatrix.append(''.join(inp.readline().strip().split()))

    ans = nXmMatrix[0].find('B') - nXmMatrix[0].rfind('A') - 1
    
    for i in range(n):
        if (nXmMatrix[i].find('B') - nXmMatrix[i].rfind('A') - 1) < ans:
            ans = nXmMatrix[i].find('B') - nXmMatrix[i].rfind('A') - 1
    
    with open('OUTPUT.txt', 'w') as out:
        out.write(str(ans))

if __name__ == '__main__':
    main()
