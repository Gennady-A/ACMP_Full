def sum_of_numbers(n):
    s = 0
    for i in n:
        s += int(i)
    return s

def is_happy(n):
    print(n)
    while len(n) != 6:
        n = '0' + n
    if sum_of_numbers(n[:int(len(n)/2)]) == sum_of_numbers(n[int(len(n)/2):]):
        return True
    return False

def main():
    answers = []
    with open('INPUT.txt', 'r') as inp:
        count = int(inp.readline().strip())
        for i in range(count):
            num = inp.readline().strip()
            if (is_happy(str(int(num)+1))) or (is_happy(str(int(num)-1))):
                answers.append('Yes')
            else:
                answers.append('No')
    with open('OUTPUT.txt', 'w') as out:
        for i in range(count):
            out.write(answers[i]+'\n')
    
if __name__ == "__main__":
    main()