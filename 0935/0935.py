def main():
    with open('INPUT.txt', 'r') as inp:
        nums = [int(i) for i in inp.read().split()]

    with open('OUTPUT.txt', 'w') as out:
        out.write('YES' if (sum(nums) % 2 == 0) else 'NO')

if __name__ == "__main__":
    main()