commands = [0, 0]
with open("INPUT.txt", "r") as inp:
    for i in range(4):
        ab = inp.readline().split()
        commands[0] += int(ab[0])
        commands[1] += int(ab[1])
        
with open("OUTPUT.txt", "w") as out:
    if commands[0] == commands[1]:
        out.write("DRAW")
    else:
        out.write(str(1+commands.index(max(commands))))