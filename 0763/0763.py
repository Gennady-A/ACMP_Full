def main():
    with open('INPUT.txt', 'r') as inp:
        n, m =[int(i) for i in inp.read().strip().split()]

    ans = ''

    if n == 1 and m == 1:
        ans = '0'
    else:
        if n == 1 or m == 1:
            ans = '1'
        else:
            ans = '2' if n == m else '1'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__  == '__main__':
    main()
