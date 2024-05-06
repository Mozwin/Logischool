maze = [
    ['#','#','#','#','#','#','#'],
    [' ',' ','#',' ',' ',' ','#'],
    ['#',' ','#','#','#','#','#'],
    ['#',' ',' ',' ','#',' ','#'],
    ['#','#','#',' ','#',' ','#'],
    ['#',' ',' ',' ',' ',' ',' '],  # cel: 5,7
    ['#','#','#','#','#','#','#']
]
poz = [1,0]

while not (poz[0] == 5 and poz[1] == 7):
    for row in range (len(maze)):
        for col in range(len(maze[row])):
            if [row,col] == poz:
                print('X', end = ' ')
            else:
                print(maze[row][col], end=' ')
        print()

    move = input("Merre menjek? (le, fel, jobbra, balra) : ").lower()

    if move == 'fel' and maze[poz[0]-1][poz[1]] != '#':
        poz = [poz[0]-1][poz[1]]

    elif move == 'le' and maze[poz[0]+1][poz[1]] != '#':
        poz = [poz[0]+1][poz[1]]

    elif move == 'jobbra' and maze[poz[0]][poz[1]+1] != '#':
        poz = [poz[0]][poz[1]+1]

    elif move == 'balra' and maze[poz[0]][poz[1]-1] != '#':
        poz = [poz[0]][poz[1]-1]
    else:
        print("ervenytelen lepes, probald ujra")
print("kijutottal")
