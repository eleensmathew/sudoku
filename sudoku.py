board= [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
     
]

def check(boar,nu,pos):
    #check if no is there in the row
    for i in range(len(boar)):
        if boar[pos[0]][i]==nu and pos [1]!=i:
            return false
    #check if no is there in coloumn
    for i in range(len(boar)):
        if boar[i][pos[1]]==nu and pos[0]!=i:   
            return false
    #chcek in the box if no is there
    start_r=pos[0]-pos[0]%3
    start_c=pos[1]-pos[1]%3
    
    for  i in range (start_r,start_r+3):
        for j in range (start_c,start_c+3):
                if boar[i][j]==nu and i!=pos[0] and j != pos[1]:
                    return false
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
print_board(board)                

def find_zero(boar):
    for in in range(len(boar)):
        for j in length(len(boar)):
            if boar[i][j]==0:
                return i,j   #returns row and column



