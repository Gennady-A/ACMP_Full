def main():
    with open('INPUT.txt', 'r') as inp:
        length = int(inp.readline())
        elements = [int(i) for i in inp.readline().strip().split()]
        elements.append(elements[0])
        elements.append(elements[1])

        maxB = 0

        for i in range(len(elements) - 2):
            if maxB < (elements[i] + elements[i+1] + elements[i+2]):
                maxB = elements[i] + elements[i+1] + elements[i+2]

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(maxB))

if __name__ == '__main__':
    main()