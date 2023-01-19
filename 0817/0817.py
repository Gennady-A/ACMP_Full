def main():
    with open('INPUT.txt', 'r') as inp:
        nums = [int(i) for i in inp.read().strip().split()]
        per = nums[0] * nums[1] * nums[2]**2
        full = (nums[0] + nums[1]) * (nums[2] * nums[3]) - per

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(full))

if __name__ == "__main__":
    main()