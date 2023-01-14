def main():

    def fib_num(c):
        f = 0
        s = 1
        for i in range(0, c):
            s = f + s
            f = s - f
        return f

    with open('INPUT.txt', 'r') as inp:
        num = int(inp.read())

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(fib_num(num)))

if __name__ == "__main__":
    main()