def countOfKruglyashi(n):
    sum = 0
    for i in n:
        if i == '0' or i == '9' or i == '6':
            sum += 1
        elif i == '8':
            sum += 2
    return sum

def main():
    with open('INPUT.txt', 'r') as inp:
        num = inp.read().strip()

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(countOfKruglyashi(num)))

if __name__ == "__main__":
    main()