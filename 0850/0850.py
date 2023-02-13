def main():
    with open('INPUT.txt', 'r') as inp:
        nums = [int(i) for i in inp.read().split()]

    ans = f'{max(nums)//2 + max(nums)%2} {min(nums)}'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()