def main():
    with open('INPUT.txt', 'r') as inp:
        x1, y1, x2, y2 = [int(i) for i in inp.readline().strip().split()]
        xA, yA = [int(i) for i in inp.readline().strip().split()]

    if x1 == x2:
        distance = abs(xA - x1)
        if x1 > xA:
            xA = x1 + distance
        else:
            xA = x1 - distance
    else:
        distance = abs(yA - y1)
        if y1 > yA:
            yA = y1 + distance
        else:
            yA = y1 - distance


    with open('OUTPUT.txt', 'w') as out:
        out.write(f'{xA} {yA}')

if __name__ == '__main__':
    main()