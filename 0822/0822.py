with open('INPUT.txt', 'r') as inp:
    n = [int(i) for i in inp.read().split()]

    a = (abs(n[0] - n[2])**2 +  abs(n[1] - n[3])**2)**0.5
    b = (abs(n[2] - n[4])**2 +  abs(n[3] - n[5])**2)**0.5
    c = (abs(n[0] - n[4])**2 +  abs(n[1] - n[5])**2)**0.5
    p = (a + b + c)/2
    s = (p * (p - a) * (p - b) * (p - c))**0.5

with open('OUTPUT.txt', 'w') as out:
    out.write(str(round(s, 1)))