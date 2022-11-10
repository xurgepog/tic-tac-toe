grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]

game = True
turn = 1
count = 0

while game == True:
    choice = True
    while choice == True:
        horizontal = int(input("Which column ")) - 1
        vertical = int(input("Which row ")) - 1
        if grid[vertical][horizontal] == 0:
            grid[vertical][horizontal] = turn
            choice = False
        else:
            print ("Invalid location")

    print (str(grid[0][0]) + "|" + str(grid[0][1]) + "|" + str(grid[0][2]))
    print ("-----")
    print (str(grid[1][0]) + "|" + str(grid[1][1]) + "|" + str(grid[1][2]))
    print ("-----")
    print (str(grid[2][0]) + "|" + str(grid[2][1]) + "|" + str(grid[2][2]))

    if grid[vertical][0] == grid[vertical][1] and grid[vertical][0] == grid[vertical][2]:
        print (str(turn) + " wins!")
        game = False 
    elif grid[0][horizontal] == grid[1][horizontal] and grid[0][horizontal] == grid[2][horizontal]:
        print (str(turn) + " wins!")
        game = False
    elif grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[1][1] != 0:
        print (str(turn) + " wins!")
        game = False
    elif grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[1][1] != 0:
        print (str(turn) + " wins!")
        game = False 
    
    count += 1
    if count == 9:
        print ("it's a tie")
        game = False

    turn *= -1
