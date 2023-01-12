def main():
    with open('INPUT.txt', 'r') as inp:
        nums = inp.read().strip()

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(max([len(i) for i in nums.split("1") if len(i) > 0] + [0])))

if __name__ == "__main__":
    main()