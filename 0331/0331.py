with open('INPUT.txt', 'r') as inp:
    start = [int(i) for i in inp.readline().split(":")]
    time = [int(i) for i in inp.readline().split()]

with open('OUTPUT.txt', 'w') as out:
    out.write(("0" if len(str(((start[0]*60 + start[1]) + (time[0]*60 + time[1]))//60%24)) == 1 else "") + str(((start[0]*60 + start[1]) + (time[0]*60 + time[1]))//60%24) + ":" + ("0" if len(str(((start[0]*60 + start[1]) + (time[0]*60 + time[1]))%60)) == 1 else "") +  str(((start[0]*60 + start[1]) + (time[0]*60 + time[1]))%60))