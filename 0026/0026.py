def main():
    with open('INPUT.txt', 'r') as inp:
        f = [int(i) for i in inp.readline().strip().split()]
        s = [int(i) for i in inp.readline().strip().split()]
        distance = (abs(f[0] - s[0])**2 + abs(f[1] - s[1])**2)**(0.5)

    with open('OUTPUT.txt', 'w') as out:
        out.write('YES' if (distance <= (f[2] + s[2])) and (abs(f[2] - s[2]) <= distance) else 'NO')

if __name__ == '__main__':
    main()