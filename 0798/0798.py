def main():
    with open('INPUT.txt', 'r') as inp:
        m, n, j, i, c = [int(a) for a in inp.read().strip().split()]

    ans = ''

    if (m * n) % 2 == 0:
        ans = 'equal'
    else:
        if (m + n) % 2 == 1:
            ans = 'white' if (((j + i) % 2 == 0 and c == 0) or ((j + i) % 2 == 1 and c == 1)) else 'black'
        else:
            ans = 'black' if (((j + i) % 2 == 0 and c == 0) or ((j + i) % 2 == 1 and c == 1)) else 'white'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()