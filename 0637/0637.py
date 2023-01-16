def main():
    with open('INPUT.txt', 'r') as inp:
        n = int(inp.readline())
        nums = [int(i) for i in inp.readline().split()]
        z = int(inp.readline())
        nums = [i if i <= z else z for i in nums]

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(sum(nums)))

if __name__ == "__main__":
    main()