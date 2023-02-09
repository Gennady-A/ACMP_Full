def main():
    with open('INPUT.txt', 'r') as inp:
        teamName = inp.readline().strip()
        teamList = []
        for i in range(3):
            teamList.append(inp.readline().strip())
        teamList.sort()

    with open('OUTPUT.txt', 'w') as out:
        out.write(f'{teamName}: {", ".join(teamList)}')

if __name__ == '__main__':
    main()