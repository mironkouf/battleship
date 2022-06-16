#MYRON KOUFOPOULOS 4398
import random
from random import randint

board3 = [' ','1','2','3','4','5']

board1 = [['a',' ',' ',' ',' ',' '],

          ['b',' ',' ',' ',' ',' '],

          ['c',' ',' ',' ',' ',' '],

          ['d',' ',' ',' ',' ',' '],

          ['e',' ',' ',' ',' ',' ']]
         
board4 = [' ','1','2','3','4','5']

board2 = [['a',' ',' ',' ',' ',' '],

          ['b',' ',' ',' ',' ',' '],
 
          ['c',' ',' ',' ',' ',' '],
 
          ['d',' ',' ',' ',' ',' '],

          ['e',' ',' ',' ',' ',' ']]
def print_board():
    print('P1 \t\t P2')
    print(' '.join(board3),end= '')
    print(' '.join(board4),)
    for i in range(5):
        print(' '.join(board1[i]) + ' '.join(board2[i]))
print_board()
print("BATTLESHIP GAME")
print("The objective is to sink the opponent's ships before the opponent sinks yours.")
p = int(input('Input 1 for 1-player game or 2 for 2-player game: '))

if p == 1:

        mironas = []

        def random_row(board2):
                    return randint(0, len(board2) - 1)
        def random_col(board2):
                    return randint(1, len(board2[0]) - 1)
        random_row(board2)
        random_col(board2)
        for i in range(5):
            ship_row = random_row(board2)
            ship_col = random_col(board2)
            x = ship_row
            y = ship_col
            o = chr(97+x)
            final_ship = str(o) + str(y)
            while final_ship in mironas:
                x=random_row(board2)
                y=random_col(board2)
                o= chr(97+x)
                final_ship = str(o) + str(y)
            mironas.append(final_ship)

        my_ships=[]

        for i in range(5):
            x=input("Player 1 enter the position of your ship no "+str(i+1)+':')
            while len(x) != 2 or x[0]<'a' or x[0]>'e' or x[1]>'5' or x[1]<'1' or x in my_ships:
                x=input("Invalid position, or position already taken. Try again: ")
            my_ships.append(x)
            
        battleship_over_i_lost = []
        battleship_over_cpu_lost = []
        player1_missiles = []
        cpu_missiles = []
        while True:
            y=input('Player 1 enter the position to throw your missile:')
            m = list(y)
            a = ord(m[0])- 97
            b = m[1]
            b = int(b)
            while len(y) != 2 or a >= 5 or b > 5 or a < 0 or b <= 0 or y in player1_missiles:
                y=input('Invalid position, or missile already thrown there. Try again:')
                m = list(y)
                a = ord(m[0])- 97
                b = m[1]
                b = int(b)
            if y in mironas:
                player1_missiles.append(y)
                print('Missile thrown at '+str(y))
                print('Target hit!')
                board2[a][b] = '0'
                battleship_over_cpu_lost.append(y)
                print_board()
                if len(battleship_over_cpu_lost) == 5:
                    print('GAME OVER. PLAYER 1 wins')
                    break
                else:
                    pass
            else:
                player1_missiles.append(y)
                print('Missile thrown at '+str(y))
                print('Target missed!')
                board2[a][b] = 'X'
                print_board()
            
            x = random_row(board1)
            y = random_col(board1)
            o = chr(97+x)
            final_ship = str(o) + str(y)
            while final_ship in cpu_missiles:
                x = random_row(board1)
                y = random_col(board1)
                o = chr(97+x)
                final_ship = str(o) + str(y)
            if final_ship in my_ships:
                    cpu_missiles.append(final_ship)
                    print('Missile thrown at '+str(final_ship))
                    print('Target hit!')
                    board1[x][y] = '0'
                    battleship_over_i_lost.append(final_ship)
                    print_board()
                    
                    if len(battleship_over_i_lost) == 5:
                        print('GAME OVER. CPU wins')
                        break
                    else:
                        pass
            else:
                    cpu_missiles.append(final_ship)
                    print('Missile thrown at '+str(final_ship))
                    print('Target missed!')
                    board1[x][y]= 'X'
                    print_board()
else:

        my_ships1=[]
        for i in range(5):
            x=input("Player 1 enter the position of your ship no "+str(i+1)+":")
            while len(x) != 2 or x[0]<'a' or x[0]>'e' or x[1]>'5' or x[1]<'1' or x in my_ships1:
                x=input("Invalid position, or position already taken. Try again: ")
            my_ships1.append(x)

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        my_ships2=[]
        for i in range(5):
            x=input("Player 2 enter the position of your ship no "+str(i+1)+":")
            while len(x) != 2 or x[0]<'a' or x[0]>'e' or x[1]>'5' or x[1]<'1' or x in my_ships2:
                x=input("Invalid position, or position already taken. Try again: ")
            my_ships2.append(x)

        battleship_player1_lost = []
        battleship_player2_lost = []
        player1_missiles = []
        player2_missiles = []

        picks = random.randint(1,2)
        if picks == 1:
            while True:
                y=input('Player 1 enter the position to throw your missile:')
                m = list(y)
                a = ord(m[0])- 97
                b = m[1]
                b = int(b)
                while len(y) != 2 or a >= 5 or b > 5 or a < 0 or b <= 0 or y in player1_missiles:
                    y=input('Invalid position, or missile already thrown there. Try again:')
                    m = list(y)
                    a = ord(m[0])- 97
                    b = m[1]
                    b = int(b)     
                if y in my_ships2:
                    player1_missiles.append(y)
                    print('Missile thrown at '+str(y))
                    print('Target hit!')
                    board2[a][b] = '0'
                    battleship_player1_lost.append(y)
                    print_board()
                    if len(battleship_player1_lost) == 5:
                        print('GAME OVER. PLAYER 1 wins')
                        break
                    else:
                        pass
                else:
                    player1_missiles.append(y)
                    print('Missile thrown at '+str(y))
                    print('Target missed!')
                    board2[a][b] = 'X'
                    print_board()

                y=input('Player 2 enter the position to throw your missile:')
                m = list(y)
                a = ord(m[0])- 97
                b = m[1]
                b = int(b)
                while len(y) != 2 or a >= 5 or b > 5 or a < 0 or b <= 0 or y in player2_missiles:
                    y=input('Invalid position, or missile already thrown there. Try again:')
                    m = list(y)
                    a = ord(m[0])- 97
                    b = m[1]
                    b = int(b)     
                if y in my_ships1:
                    player2_missiles.append(y)
                    print('Missile thrown at '+str(y))
                    print('Target hit!')
                    board1[a][b] = '0'
                    battleship_player2_lost.append(y)
                    print_board()
                    if len(battleship_player2_lost) == 5:
                        print('GAME OVER. PLAYER 2 wins')
                        break
                    else:
                        pass
                else:
                    player2_missiles.append(y)
                    print('Missile thrown at '+str(y))
                    print('Target missed!')
                    board1[a][b] = 'X'
                    print_board()
        else:
                while True:
                    y=input('Player 2 enter the position to throw your missile:')
                    m = list(y)
                    a = ord(m[0])- 97
                    b = m[1]
                    b = int(b)
                    while len(y) != 2 or a >= 5 or b > 5 or a < 0 or b <= 0 or y in player2_missiles:
                        y=input('Invalid position, or missile already thrown there. Try again:')
                        m = list(y)
                        a = ord(m[0])- 97
                        b = m[1]
                        b = int(b)     
                    if y in my_ships1:
                        player2_missiles.append(y)
                        print('Missile thrown at '+str(y))
                        print('Target hit!')
                        board1[a][b] = '0'
                        battleship_player2_lost.append(y)
                        print_board()
                        if len(battleship_player2_lost) == 5:
                            print('GAME OVER. PLAYER 2 wins')
                            break
                        else:
                            pass
                    else:
                        player2_missiles.append(y)
                        print('Missile thrown at '+str(y))
                        print('Target missed!')
                        board1[a][b] = 'X'
                        print_board()

                    y=input('Player 1 enter the position to throw your missile:')
                    m = list(y)
                    a = ord(m[0])- 97
                    b = m[1]
                    b = int(b)
                    while len(y) != 2 or a >= 5 or b > 5 or a < 0 or b <= 0 or y in player1_missiles:
                        y=input('Invalid position, or missile already thrown there. Try again:')
                        m = list(y)
                        a = ord(m[0])- 97
                        b = m[1]
                        b = int(b)     
                    if y in my_ships2:
                        player1_missiles.append(y)
                        print('Missile thrown at '+str(y))
                        print('Target hit!')
                        board2[a][b] = '0'
                        battleship_player1_lost.append(y)
                        print_board()
                        if len(battleship_player1_lost) == 5:
                            print('GAME OVER. PLAYER 1 wins')
                            break
                        else:
                            pass
                    else:
                        player1_missiles.append(y)
                        print('Missile thrown at '+str(y))
                        print('Target missed!')
                        board2[a][b] = 'X'
                        print_board()