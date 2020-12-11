with open('input11.txt') as f:
    grid = f.read()
    grids = [[list(n) for n in grid.split()],[list(n) for n in grid.split()]]

def print_chairs(grid):
    print('\n'.join(''.join(g) for g in grid))


def musical_chairs(grids):
    height = len(grids[0])
    width = len(grids[0][0])
    def check_neighbors(g,x,y):
        occupied = free_chair = 0
        for yy in range(max(y-1,0),min(y+1,height-1)+1):
            for xx in range(max(x-1,0),min(x+1,width-1)+1):
                if xx == x and yy == y:
                    #self chair, ignore
                    continue
                elif grids[g][yy][xx] == '#':
                    occupied += 1
                elif grids[g][yy][xx] == 'L':
                    free_chair += 1
        return occupied, free_chair

    unmodified = False
    reading_grid = 0
    seats_taken = 0

    while unmodified == False:
        unmodified = True
        reading_grid += 1
        #print_chairs(grids[reading_grid%2])
        for y in range(height):
            for x in range(width):
                spot = grids[reading_grid%2][y][x]
                if spot == '.':
                    #Just a floor, moving on
                    continue
                occud, freed = check_neighbors(reading_grid%2,x,y)
                if spot == 'L' and occud == 0:
                    grids[(reading_grid+1)%2][y][x] = '#'
                    seats_taken += 1
                    unmodified = False
                elif spot == '#' and occud >= 4:
                    grids[(reading_grid+1)%2][y][x] = 'L'
                    unmodified = False
                    seats_taken -= 1
                else:
                    grids[(reading_grid+1)%2][y][x] = spot
    return seats_taken

def musical_chairs2(grids):
    height = len(grids[0])
    width = len(grids[0][0])
    def check_neighbors(g,x,y):
        occupied = free_chair = 0
        for yy in range(max(y-1,0),min(y+1,height-1)+1):
            for xx in range(max(x-1,0),min(x+1,width-1)+1):
                if xx == x and yy == y:
                    #self chair, ignore
                    continue
                elif grids[g][yy][xx] == '#':
                    occupied += 1
                elif grids[g][yy][xx] == 'L':
                    free_chair += 1
                elif grids[g][yy][xx] == '.':
                    offx,offy = xx-x,yy-y
                    i = 1
                    while 0<=(x+offx*i)<width and 0<=(y+offy*i)<height:
                        spot = grids[g][y+offy*i][x+offx*i]
                        if spot == '#':
                            occupied += 1
                            break
                        elif spot == 'L':
                            free_chair += 1
                            break
                        elif spot == '.':
                            i += 1
        return occupied, free_chair

    unmodified = False
    reading_grid = 0
    seats_taken = 0

    while unmodified == False:
        unmodified = True
        reading_grid += 1
        #print_chairs(grids[reading_grid%2])
        for y in range(height):
            for x in range(width):
                spot = grids[reading_grid%2][y][x]
                if spot == '.':
                    #Just a floor, moving on
                    continue
                occud, freed = check_neighbors(reading_grid%2,x,y)
                if spot == 'L' and occud == 0:
                    grids[(reading_grid+1)%2][y][x] = '#'
                    seats_taken += 1
                    unmodified = False
                elif spot == '#' and occud >= 5:
                    grids[(reading_grid+1)%2][y][x] = 'L'
                    unmodified = False
                    seats_taken -= 1
                else:
                    grids[(reading_grid+1)%2][y][x] = spot
    return seats_taken

seats = musical_chairs2(grids)
print(seats)