grid=[["_" for i in range(3)] for j in range(3)]
def print_grid():
    for i in range(3):
        for j in range(3):
            print(grid[i][j],end=" ")
        print()
print_grid()
def win():

    for i in range(3):

        cur=set(grid[i])
        if len(cur)==1 and grid[i][0]=="O":
            print("Player 1 wins")
            return True
        elif len(cur)==1 and grid[i][0]=="X":
            print("Player 2 wins")
            return True
    for i in range(3):
        cur=set([grid[j][i] for j in range(3)])
        if len(cur)==1 and grid[0][i]=="O":
            print("Player 1 wins")
            return True
        elif len(cur)==1 and grid[0][i]=="X":
            print("Player 2 wins")
            return True
    cur=set([grid[i][i] for i in range(3)])
    if len(cur)==1 and grid[0][0]=="O":
        print("Player 1 wins")
        return True
    elif len(cur)==1 and grid[0][0]=="X":
        print("Player 2 wins")
        return True
    cur=set([grid[i][2-i] for i in range(3)])
    if len(cur)==1 and grid[0][2]=="O":
        print("Player 1 wins")
        return True
    elif len(cur)==1 and grid[0][2]=="X":
        print("Player 2 wins")
        return True
    return False
def draw():
    for i in range(3):
        for j in range(3):
            if grid[i][j]=="_":
                return False
    print("Draw")
    return True

cur=0
while True:

    if draw():
        break
    
    if cur==0:
        print("Player 1")
        row=int(input("Enter row: "))-1
        col=int(input("Enter col: "))-1
        if grid[row][col]!="_":
            print("Invalid move")
            continue
    
        grid[row][col]="O"
        print_grid()
        if win():
            break
        cur=1
    
    else:
        print("Player 2")
        
        row=int(input("Enter row: "))-1
        
        col=int(input("Enter col: "))-1
        
        if grid[row][col]!="_":
            print("Invalid move")
            continue
        grid[row][col]="X"
        print_grid()
        if win():
            break
        
        cur=0
print("Game Over")
    