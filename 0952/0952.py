def main():
    with open('INPUT.txt', 'r') as inp:
        a, c = [int(i) for i in inp.read().strip().split()]

    if a == 0 and c > 0:
        ans = 'Impossible'
    else:
        ans = str(a + ((c - a) if c >= a else 0) * 1) + ' ' + str(a + (c - 1 if c > 0 else 0))

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()