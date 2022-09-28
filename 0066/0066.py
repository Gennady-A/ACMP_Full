alphabet = "qwertyuiopasdfghjklzxcvbnm"

with open('INPUT.txt', 'r') as inp:
    letter = inp.read().strip()

with open('OUTPUT.txt', 'w') as out:
    out.write(alphabet[alphabet.index(letter) + 1] if alphabet.index(letter) + 1 != len(alphabet) else "q")