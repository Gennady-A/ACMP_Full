def main():
    with open('INPUT.txt', 'r') as inp:
        field = [list(inp.readline().strip()) for i in range(3)]

    ans = ''

    if (field[0][0] == field[1][1] and field[1][1] == field[2][2]) or (field[0][2] == field[1][1] and field[1][1] == field[2][0]):
        if field[1][1] == 'X':
            ans = 'Win'
        else:
            ans = 'Lose'
    else:
        for i in range(3):
            if (field[i][0] == field[i][1] and field[i][1] == field[i][2] and field[i][0] == 'X') or (field[0][i] == field[1][i] and field[1][i] == field[2][i] and field[0][i] == 'X'):
                ans = 'Win'
                break
            elif (field[i][0] == field[i][1] and field[i][1] == field[i][2] and field[i][0] == 'O') or (field[0][i] == field[1][i] and field[1][i] == field[2][i] and field[0][i] == 'O'):
                ans = 'Lose'
                break
            ans = 'Draw'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()