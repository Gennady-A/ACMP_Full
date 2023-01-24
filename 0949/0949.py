def main():
    with open('INPUT.txt', 'r') as inp:
        n, f, s = [int(i) for i in inp.read().strip().split()]

    for i in range(n, 1, -1):
        f = s - f
        s = s - f

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(f) + ' ' + str(s))

if __name__ == '__main__':
    main()