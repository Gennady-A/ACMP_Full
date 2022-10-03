with open('INPUT.txt', 'r') as inp:
    nums = [int(i) for i in inp.readline().split()]
    mod = inp.readline().strip()

with open('OUTPUT.txt', 'w') as out:
    out.write(str(min(nums)) if mod == "freeze" else str(max(nums)) if mod == "heat" else str(nums[1]) if mod == "auto" else str(nums[0]))