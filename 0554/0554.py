def main():
    with open('INPUT.txt', 'r') as inp:
        n = int(inp.read().strip())
    
    ans = str(int((n+1)*n/2+1))

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()