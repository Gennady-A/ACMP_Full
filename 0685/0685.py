with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.read().split()]
    allA = nums[:3]
    allB = nums[3:]
    allA.sort()
    allB.sort()

with open('OUTPUT.txt', 'w') as out:
    out.write(str(sum([allA[i] * allB[i] for i in range(3)])))