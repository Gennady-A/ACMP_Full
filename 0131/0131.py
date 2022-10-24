max = 0
maxI = -1
with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    for i in range(count):
        nums = [int(i) for i in inp.readline().split()]
        if nums[1] == 1:
            if nums[0] > max:
                max = nums[0]
                maxI = i + 1    

with open('OUTPUT.txt', 'w') as out:
    out.write(str(maxI))