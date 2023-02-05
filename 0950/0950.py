def main():
    with open('INPUT.txt', 'r') as inp:
        binary = inp.read()

    alphabet = ['a', 'b', 'c', 'd', 'e', 
                'f', 'g', 'h', 'i', 'j', 
                'k', 'l', 'm', 'n', 'o', 
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 
                'z']

    ans = ''.join([alphabet[len(i)] for i in binary.split('1')])

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans[:-1])

if __name__ == '__main__':
    main()