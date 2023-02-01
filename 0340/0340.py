def main():

    with open('INPUT.txt', 'r') as inp:
        Box1 = [int(i) for i in inp.readline().strip().split()]
        Box2 = [int(i) for i in inp.readline().strip().split()]
        
        ans = ''

        Box1.sort()
        Box2.sort()
        Difference = [Box1[i] - Box2[i] for i in range(3)]

        if Difference[0] == 0 and Difference[1] == 0 and Difference[2] == 0:
            ans = 'Boxes are equal'
        else:
            if min(Difference) < 0 and max(Difference) > 0:
                ans = 'Boxes are incomparable'
            else: 
                if sum(Difference) < 0:
                    ans = 'The first box is smaller than the second one'
                elif sum(Difference) > 0:
                    ans = 'The first box is larger than the second one'
                else:
                    ans = 'Boxes are incomparable'

    with open('OUTPUT.txt', 'w') as out:
        out.write(ans)

if __name__ == '__main__':
    main()