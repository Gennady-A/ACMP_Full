def main():
    with open('INPUT.txt', 'r') as inp:
        K = int(inp.read().strip())

    ans = 0

    while K != 1:
        K -= 1
        ans += 5
        if ans / 60 > 12:
            ans = 'NO'
            break
    
    if ans != 'NO':
        ans = f'{ans//60} {ans%60}'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()