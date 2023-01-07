def main():
    with open('INPUT.txt', 'r') as inp:
        nums = [int(i) for i in inp.readline().split()]

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(abs(nums[1] - nums[2])-1) if abs(nums[1] - nums[2]) < (nums[0] - abs(nums[1] - nums[2])) else str((nums[0] - abs(nums[1] - nums[2])) - 1))

if __name__ == "__main__":
    main()