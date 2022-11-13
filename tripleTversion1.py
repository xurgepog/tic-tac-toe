class Boardsetup:
    def __init__(self):
        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]

gameboard = Boardsetup()

game = True
turn = 1
count = 0

while game == True:
    choice = True
    while choice == True:
        horizontal = int(input("Which column ")) - 1
        vertical = int(input("Which row ")) - 1
        if gameboard.grid[vertical][horizontal] == 0:
            gameboard.grid[vertical][horizontal] = turn
            choice = False
        else:
            print ("Invalid location")

    print (str(gameboard.grid[0][0]) + "|" + str(gameboard.grid[0][1]) + "|" + str(gameboard.grid[0][2]))
    print ("-----")
    print (str(gameboard.grid[1][0]) + "|" + str(gameboard.grid[1][1]) + "|" + str(gameboard.grid[1][2]))
    print ("-----")
    print (str(gameboard.grid[2][0]) + "|" + str(gameboard.grid[2][1]) + "|" + str(gameboard.grid[2][2]))

    if gameboard.grid[vertical][0] == gameboard.grid[vertical][1] and gameboard.grid[vertical][0] == gameboard.grid[vertical][2]:
        print (str(turn) + " wins!")
        game = False 
    elif gameboard.grid[0][horizontal] == gameboard.grid[1][horizontal] and gameboard.grid[0][horizontal] == gameboard.grid[2][horizontal]:
        print (str(turn) + " wins!")
        game = False
    elif gameboard.grid[0][0] == gameboard.grid[1][1] and gameboard.grid[0][0] == gameboard.grid[2][2] and gameboard.grid[1][1] != 0:
        print (str(turn) + " wins!")
        game = False
    elif gameboard.grid[0][2] == gameboard.grid[1][1] and gameboard.grid[0][2] == gameboard.grid[2][0] and gameboard.grid[1][1] != 0:
        print (str(turn) + " wins!")
        game = False 
    
    count += 1
    if count == 9:
        print ("it's a tie")
        game = False

    turn *= -1