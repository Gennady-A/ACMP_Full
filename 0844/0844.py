def main():
    with open('INPUT.txt', 'r') as inp:
        nums = [int(i) for i in inp.read().split()]

        S = nums[0] * nums[1] 

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(int(S**(0.5))) if int(S**(0.5)) == S**(0.5) else '0')

if __name__ == "__main__":
    main()