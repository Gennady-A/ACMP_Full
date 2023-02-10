def main():
    with open('INPUT.txt', 'r') as inp:
        n = int(inp.read())

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(n + str(bin(n)).count('1')))

if __name__ == '__main__':
    main()