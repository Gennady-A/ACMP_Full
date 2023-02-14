def main(): 
    with open('INPUT.txt', 'r') as inp:
        n, s = [int(i) for i in inp.readline().strip().split()]
        a = [int(i) for i in inp.readline().strip().split()]
        a.sort()

    aCount = 0

    for i in range(len(a)):
        if min(a) <= s:
            s -= a.pop(a.index(min(a)))
            aCount += 1
        else:
            break

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(aCount))

if __name__ == '__main__':
    main()