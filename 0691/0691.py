def main():
    letters = ['A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y']

    with open('INPUT.txt', 'r') as inp:
        count = inp.readline()
        nums = []
        for i in range(int(count)):
            nums.append(inp.readline())

    with open('OUTPUT.txt', 'w') as out:
        for num in nums:
            if (len(num.strip()) == 6) and (num[0] in letters) and (num[1:3].isdigit()) and (num[4] in letters) and (num[5] in letters):
                out.write('Yes\n')
            else:
                out.write('No\n')

if __name__ == "__main__":
    main()