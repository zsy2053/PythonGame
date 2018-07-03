def board(x, chang, kuan, pla):
    for i in range(len(x)):
        print('|', end="")
        for j in range (len(x[i])):
            if chang and kuan and i == int(chang) and j == int(kuan):
                if pla == 0:
                    x[i][j] = 'X'
                    print(' X ')
                else:
                    x[i][j] = 'O'
                    print(' O ')
            else:
                print(' ' + str(x[i][j]) + ' ', end="")
        print('|')

def startGame():
    x = [ [0, 1], [2, 3], [4, 5] ]
    while(1):
        board(x, None, None, None)
        p1_w = input('Please Enter the width number for player 1, enter q to exit')
        if p1_w == 'q':
            print("Good Bye")
            break
        p1_h = input('Please Enter the height number for player 1, enter q to exit')
        if p1_h == 'q':
            print("Good Bye")
            break
        p1_con = input('Are you Sure about your move?(y or n), enter q to exit')
        if p1_con == 'q':
            print("Good Bye")
            break
        if p1_con == 'y':
            board(x, p1_w, p1_h, 0)
            while(1):
                p2_w = input('Please Enter the width number for player 2, enter q to back to player1')
                if p2_w == 'q':
                    print("Back to player 1")
                    break
                p2_h = input('Please Enter the height number for player 2, enter q to back to player1')
                if p2_h == 'q':
                    print("Back to player 1")
                    break
                p2_con = input('Are you Sure about your move?(y or n), enter q to back to player1')
                if p2_con == 'q':
                    print("Back to player 1")
                    break
                elif p2_con == 'y':
                    board(x, p2_w, p2_h, 1)
                else:
                    continue
        else:
            continue

startGame()
