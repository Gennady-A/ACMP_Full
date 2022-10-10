with open('INPUT.txt', 'r') as inp:
    num, word = inp.read().split()

with open('OUTPUT.txt', 'w') as out:
    out.write(word.strip()[:int(num)-1] + word.strip()[:int(num)-1:-1][::-1])