def main():
    with open('INPUT.txt', 'r') as inp:
        ans = int(sum([int(i) for i in inp.read().strip().split()]) / 27)

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(ans))

if __name__ == '__main__':
    main()