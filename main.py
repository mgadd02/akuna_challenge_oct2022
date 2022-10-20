import random

def display_game(game, size):
    #header
    header = "  | "
    for z in range(0, size):
        header += (str(z) + " ")
    print(header)
    print("- " * (size + 2))
    #main rows 
    for x in range(0, size):
        row = str(x) + " | "
        for y in range (0, size):
            row += (str(game[x][y]) + " ")
        print(row)

def rNum(options):
    return random.randint(1,options)

def getValidDir(x,y,size, freedom):
    response = " "
    changes = 0
    for count in range (0, 4):
        if (y+1 < size and changes < freedom):
            response = ">"
            changes += 1
        if (y > 0 and changes < freedom):
            response = "<"
            changes += 1
        if (x+1 < size and changes < freedom):
            response = "v"
            changes += 1
        if (x > 0 and changes < freedom):
            response = "^"
            changes += 1
    return response

def calculate(grid, size):
    for x in range(0, size):
        for y in range(0, size):
            direction = 0
            if (x == 0 or x == size-1):
                if (y == 0 or y == size-1):
                    direction = getValidDir(x,y,size, rNum(2))
                else:
                    direction = getValidDir(x,y,size, rNum(3))
            elif (y == 0 or y == size-1):
                if (x == 0 or x == size-1):
                    direction = getValidDir(x,y,size, rNum(2))
                else:
                    direction = getValidDir(x,y,size, rNum(3))
            else:
                direction = getValidDir(x,y,size, rNum(4))
            grid[x][y] = direction

def count(grid, size):
    total = 0
    for x in range (0, size):
        for y in range(0, size):
            curr = grid[x][y]
            if (curr == "v" and grid[x+1][y] == "^"):
                total += 1
                grid[x+1][y] = "X"
                grid[x][y] = "X"
            if (curr == "^" and grid[x-1][y] == "v"):
                total += 1
                grid[x-1][y] = "X"
                grid[x][y] = "X"
            if (curr == ">" and grid[x][y+1] == "<"):
                total += 1
                grid[x][y+1] = "X"
                grid[x][y] = "X"
            if (curr == "<" and grid[x][y-1] == ">"):
                total += 1
                grid[x][y-1] = "X"
                grid[x][y] = "X"
    return total


#main
#initialise vars
print("\n-Executing program.-\n")
size = int(input("Grid size: "))
loopNum = int(input("Number of trials: "))
highFives = 0
runningTotal = 0
# 0 if no repeated prints, 1 to show steps
verbose = int(input("Verbose Mode: "))
#init game grid with zeros
grid = [[0 for x in range(size)] for y in range(size)] 
print("\nRunning " + str(loopNum) + " trials...\n")
for counter in range(0, loopNum):
    #calculate a grid
    calculate(grid, size)
    #display grid
    if (verbose):
        print("Iteration: " + str(counter+1))
        display_game(grid, size)
    highFives = count(grid, size)
    if (verbose):
        print("High-Fives at: ")
        display_game(grid, size)
    runningTotal += highFives
    if (verbose):
        print("High Fives: " + str(highFives) + "\n")
    
print("Average: " + str(runningTotal/loopNum) + "\n")
print("Done.")