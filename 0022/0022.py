def sum_of_one(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        r = n % 2
        n = n // 2
        return r + sum_of_one(n)

def main():
    with open('INPUT.txt', 'r') as inp:
        num = int(inp.read().strip())

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(sum_of_one(num)))


if __name__ == "__main__":
    main()