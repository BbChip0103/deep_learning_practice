#import sys, os
#sys.path.append(os.path.curdir)
import Gate

if __name__ == '__main__' :
    print('And Gate')
    for i in range(0, 2) :
        for j in range(0, 2) :
            print( '%d & %d = %d' %(i, j, Gate.AndGate(i, j)) )
    print('')

    print('Nand Gate')
    for i in range(0, 2) :
        for j in range(0, 2) :
            print( '%d & %d = %d' %(i, j, Gate.NandGate(i, j)) )
    print('')

    print('Or Gate')
    for i in range(0, 2) :
        for j in range(0, 2) :
            print( '%d & %d = %d' %(i, j, Gate.OrGate(i, j)) )
    print('')

    print('Nor Gate')
    for i in range(0, 2) :
        for j in range(0, 2) :
            print( '%d & %d = %d' %(i, j, Gate.NorGate(i, j)) )
    print('')

    print('Xor Gate')
    for i in range(0, 2) :
        for j in range(0, 2) :
            print( '%d & %d = %d' %(i, j, Gate.XorGate(i, j)) )
    print('')
