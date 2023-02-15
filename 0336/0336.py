def main():
    with open('INPUT.txt', 'r') as inp:
        n = inp.readline().strip()

    tNow = 0
    minT = 0
    maxT = 0

    for i in n:
        if i == '1':
            tNow -= 1
        else:
            tNow += 1
        
        if tNow < minT:
            minT = tNow
        if tNow > maxT:
            maxT = tNow
    
    distance = abs(maxT - minT) + 1

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(distance))

if __name__ == '__main__':
    main()