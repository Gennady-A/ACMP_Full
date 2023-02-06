def main():
    with open('INPUT.txt', 'r') as inp:
        num = int(inp.read())

    sum = 0

    if num > 0:
        for i in range(1, num+1):
            sum += i
    else:
        for i in range(num, 2):
            sum += i


    with open('OUTPUT.txt', 'w') as out:
        out.write(str(sum))

if __name__ == '__main__':
    main()