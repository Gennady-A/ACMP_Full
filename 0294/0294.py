def main():
    with open('INPUT.txt', 'r') as inp:
        f = [int(i) for i in inp.readline().strip().split()]
        s = [int(i) for i in inp.readline().strip().split()]

    k1After = int(f[0] * (100-f[1]) / 100)
    k2After = int(s[0] * (100-s[1]) / 100)

    res = (f[0] * f[2] + s[0] * s[2]) - min([k1After, k2After]) * (f[2] + s[2])

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(res))
    

if __name__ == "__main__":
    main()