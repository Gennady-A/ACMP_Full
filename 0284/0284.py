with open('INPUT.txt', 'r') as inp:
    nums_len = int(inp.readline())
    nums = inp.readline().split()
    count = int(inp.readline())
    ans = ""
    for i in range(count):
        sl = [int(i) for i in inp.readline().split()]
        ans += " ".join(nums[sl[0]-1:sl[1]]) + "\n"

with open('OUTPUT.txt', 'w') as out:
    out.write(ans)