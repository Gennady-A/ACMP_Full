with open('INPUT.txt', 'r') as inp:
    count = int(inp.readline())
    nums = [inp.readline().split() for i in range(count)]
    nums = [int(19 * int(nums[i][1]) + (int(nums[i][0]) + 239) * (int(nums[i][0]) + 366) / 2)  for i in range(count)]

with open('OUTPUT.txt', 'a') as out:
    for i in range(count):
        out.write(str(nums[i]) + '\n' if i != len(nums) - 1 else str(nums[i]))