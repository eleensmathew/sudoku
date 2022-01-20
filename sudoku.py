board=[]
for i in range(9):
    board=board+[eval(input('Enter list of 9 numbers\n Enter 0 for blanks: '))]


def check(boar,nu,pos):
    #check if no is there in the row
    for i in range(len(boar)):
        if boar[pos[0]][i]==nu and pos [1]!=i:
            return False
    #check if no is there in coloumn
    for i in range(len(boar)):
        if boar[i][pos[1]]==nu and pos[0]!=i:   
            return False
    #chcek in the box if no is there
    start_r=pos[0]-pos[0]%3
    start_c=pos[1]-pos[1]%3
    
    for  i in range (start_r,start_r+3):
        for j in range (start_c,start_c+3):
                if boar[i][j]==nu and i!=pos[0] and j != pos[1]:
                    return False
    return True                  

def print_board(boar):    #prints the board
    for i in range (len (boar)):
        if i % 3==0 and i != 0:
            print('- '*14)
        for j in range(len(boar[0])):
            if j% 3 ==0 and j!=0:
                print('|',end='')
            if j==8:
                print(boar[i][j])
            else:
                print(str(boar[i][j])+' ',end='')

def find_zero(boar):
    for i in range(len(boar)):
        for j in range(len(boar)):
            if boar[i][j]==0:
                return i,j   #returns row and column
    return None
#checks if we solved the puzzle
def solve(boar):
    find = find_zero(boar)
    if not find:
        return True
    else:
        row,col=find
    for i in range (1,10):
            if check(boar,i,(row,col)):
                boar[row][col]=i
                if solve(boar):
                    return True
                boar[row][col]=0
    return False 

print_board(board)
print()
print()
solve(board)
print_board(board)
     
