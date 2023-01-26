def main():
    with open('INPUT.txt', 'r') as inp:
        size = int(inp.readline())
        matrix = []
        for i in range(size):
            matrix.append([int(i) for i in inp.readline().strip().split()])

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(int(sum([sum(i) for i in matrix])/2)))

if __name__ == '__main__':
    main()