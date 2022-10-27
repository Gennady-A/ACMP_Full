with open('INPUT.txt', 'r') as inp:
    pos = int(inp.read())
    nums = [pos-8, pos+8, 0 if pos%8 == 0 else pos+1, 0 if pos%8 == 1 else pos-1]
    nums.sort()
    ans = ""
    for i in nums:
        if i <= 64 and i >= 1:
            ans += str(i) + " "
    nums = list(map(str, nums))

with open('OUTPUT.txt', 'w') as out:
    out.write(ans)