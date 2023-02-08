def main():
    with open('INPUT.txt', 'r') as inp:
        gopherX, gopherY = [int(i) for i in inp.readline().strip().split()]
        dogX, dogY = [int(i) for i in inp.readline().strip().split()]
        burrowCount = int(inp.readline().strip())
        burrows = []
        for i in range(burrowCount):
            burrows.append([int(i) for i in inp.readline().strip().split()])

    ans = 'NO'
    for i in burrows:
        dogDistance = (abs(dogX - i[0])**2 + abs(dogY - i[1])**2)**(0.5)
        gopherDistance = (abs(gopherX - i[0])**2 + abs(gopherY - i[1])**2)**(0.5)
        if not(dogDistance < gopherDistance * 2):
            ans = str(burrows.index(i) + 1)
            break

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()