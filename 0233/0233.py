with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    nums = [int(i) for i in inp.readline().split()]

with open('OUTPUT.txt', 'w') as out:
    for i in range(len(nums)):
        if nums[i] <= 437:
            out.write("Crash " + str(i+1))
            break
        else:
            count -= 1
    if count == 0:
        out.write("No crash")