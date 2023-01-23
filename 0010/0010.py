def main():
    with open('INPUT.txt', 'r') as inp:
        coefs = [int(i) for i in inp.read().strip().split()]

    with open('OUTPUT.txt', 'w') as out:
        out.write(' '.join([str(i) for i in range(-100, 101) if (coefs[0] * i**3 + coefs[1] * i**2 + coefs[2] * i + coefs[3]) == 0]))

if __name__ == '__main__':
    main()