def main():
    with open('INPUT.txt', 'r') as inp:
        S, P = [int(i) for i in inp.read().strip().split()]

    for i in range(S):
        if i * (S - i) == P:
            with open('OUTPUT.txt', 'w') as out:
                out.write('{0} {1}'.format(i, S - i))
            break

if __name__ == '__main__':
    main()