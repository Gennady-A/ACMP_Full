def main():
    with open('INPUT.txt', 'r') as inp:
        f, s = [int(i) for i in inp.readline().strip().split()]
    
    ans = max([f, s])

    while (ans % f != 0) or (ans % s != 0):
        ans += max([f, s])

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(ans))
    
if __name__ == '__main__':
    main()
    