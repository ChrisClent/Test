from random import randint
from copy import deepcopy
SIZE=12

def genRandBoard(size):
    board=[]
    for r in range(size):
        board.append([])
        for c in range(size):
            #coin flip
            flip=randint(0,1)
            #if true, enter an X
            if(flip):
                board[r].append("X")
            else:
                board[r].append(" ")
    return board


#cell is 0,0 position
#examine its neighbors
#return neigbors relative to cell
def countNeighbors(board,r,c):
    neighbors=0
    for i in range(-1,2):
        for j in range(-1,2):
            #skip 0,0 case, examine adjacent cells
            if not( i==0 and j==0):
                #check OOB
                if not((r==0 and i==-1)or
                       (c==0 and j==-1)or
                       (r==len(board)-1 and i==1)or
                       (c==len(board)-1 and j==1)):
                    #if appropriate, check neighbors
                    if board[r+i][c+j]=="X":
                       neighbors+=1        
    return neighbors

def calcNextGen(board):
    #keep original board
    nextBoard=deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            #count neighbors
            neighbors=countNeighbors(board,r,c)
            #apply the conway GOL rules for living cells
            if board[r][c]=="X":
                #make decisions based on rules
                if neighbors<2 or neighbors >3 :
                    nextBoard[r][c]=" "
            else:
                #see if dead cell should live
                if neighbors==3:
                    nextBoard[r][c]="X"
    return nextBoard
            

#display board function
def dispBoard(board):
    #print column number
    print(" ",end=" ")
    for l in range(len(board)):
        print(l%10,end=" ")
    print()
    for r in range(len(board)):
        #current row number
        print(r%10,end="|")
        for c in range(len(board[0])):
            print(board[r][c],end="|")
        print()

#create a canned board
##master=[ ['x',' ',' '],
##         [' ',' ','x'],
##         [' ','x',' '] ]
board=genRandBoard(SIZE)

#print board
dispBoard(board)
board = calcNextGen(board)

print()
print()

dispBoard(board)
