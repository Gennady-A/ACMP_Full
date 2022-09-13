with open("INPUT.txt", "r") as inp:
    nums = [int(i) for i in inp.read().split()]

with open("OUTPUT.txt", "w") as out:
    out.write("Error" if min(nums) < 94 or max(nums) > 727 else str(max(nums)))