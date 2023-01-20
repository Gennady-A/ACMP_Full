def main():
    with open('INPUT.txt', 'r') as inp:
        count = inp.readline()
        allDay = ''.join(list(map(lambda x: '1' if int(x) > 0 else '0', inp.readline().strip().split())))
        length = max([len(i) for i in allDay.split('0')])

    with open('OUTPUT.txt', 'w') as out:
        out.write(str(length))

if __name__ == '__main__':
    main()