def main():
    with open('INPUT.txt', 'r') as inp:
        HxW = [int(i) for i in inp.readline().strip().split()]
        orig = ''
        for i in range(HxW[0]):
            orig += inp.readline().strip()

        inp.readline()

        neg = ''
        for i in range(HxW[0]):
            neg += inp.readline().strip()

        wrong = 0
        for i in range(len(neg)):
            if neg[i] == orig[i]:
                wrong += 1

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(wrong))

if __name__ == '__main__':
    main()