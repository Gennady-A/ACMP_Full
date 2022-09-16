with open("INPUT.txt", "r") as inp:
    count = int(inp.readline())
    nums = [int(inp.readline()) for i in range(count)]

with open("OUTPUT.txt", "w") as out:
    out.write(str(nums.count(0)) if nums.count(0) < nums.count(1) else str(nums.count(1)))