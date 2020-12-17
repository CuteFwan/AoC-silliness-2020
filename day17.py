grid = dict()

with open('input17.txt') as f:
    grid_input = [list(g) for g in f.read().split()]
    width = len(grid_input[0])
    height = len(grid_input)
    
    for y in range(0, height):
        for x in range(0, width):
            cube = grid_input[y][x]
            if cube == '#':
                grid[x,y,0,0] = grid_input[y][x]

def look_around(grid, x, y, z):
    active = 0
    for k in range(z-1, z+2):
        for j in range(y-1, y+2):
            for i in range(x-1, x+2):
                if i == x and j == y and k == z:
                    continue
                if grid.get((i,j,k,0), None):
                    active += 1
    return active

def look_around3(grid, x, y, z, w):
    active = 0
    for ww in range(w-1, w+2):
        for k in range(z-1, z+2):
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if i == x and j == y and k == z and ww == w:
                        continue
                    if grid.get((i,j,k,ww), None):
                        active += 1
    return active

def print_grid(grid):
    msg = ''
    for z in range(z_min, z_max):
        msg += f'z={z}\n'
        for y in range(y_min, y_max):
            layer = ' '
            for x in range(x_min, x_max):
                layer += grid.get((x,y,z,0),'.')
            msg += layer + '\n'
        msg += '\n'
    print(msg)

def print_grid3(grid):
    msg = ''
    for w in range(w_min, w_max):
        for z in range(z_min, z_max):
            msg += f'z={z} y={w}\n'
            for y in range(y_min, y_max):
                layer = ' '
                for x in range(x_min, x_max):
                    layer += grid.get((x,y,z,w),'.')
                msg += layer + '\n'
            msg += '\n'
    print(msg)
def part1(g, width, height):
    grid = {k: v for k, v in g.items()}
    x_min, x_max = 0, width
    y_min, y_max = 0, height
    z_min, z_max = 0, 1
    w_min, w_max = 0, 1
    for _ in range(6):
        new_grid = dict()
        exp_x = exp_y = exp_z = False
        for z in range(z_min-1, z_max+1):
            for y in range(y_min-1, y_max+1):
                for x in range(x_min-1, x_max+1):
                    neighbors = look_around(grid,x,y,z)
                    #print(f'{x,y,z}: {neighbors}')
                    if 2 <= neighbors <= 3:
                        state = bool(grid.get((x,y,z,0), None))
                        if state or (not state and neighbors == 3):
                            #print(f'{x,y,z}: {state},{neighbors}')
                            new_grid[x,y,z,0] = '#'
                            if not (x_min < x < x_max):
                                exp_x = True
                            if not (y_min < y < y_max):
                                exp_y = True
                            if not (z_min < z < z_max):
                                exp_z = True
        if exp_x:
            #print('expanding x')
            x_min -=1
            x_max +=1
        if exp_y:
            #print('expanding y')
            y_min -=1
            y_max +=1
        if exp_z:
            #print('expanding z')
            z_min -=1
            z_max +=1
        grid = new_grid
        #print_grid(grid)
    print(len(grid))
def part2(g, width, height):
    grid = {k: v for k, v in g.items()}
    x_min, x_max = 0, width
    y_min, y_max = 0, height
    z_min, z_max = 0, 1
    w_min, w_max = 0, 1
    for _ in range(6):
        new_grid = dict()
        exp_x = exp_y = exp_z = exp_w = False
        for w in range(w_min-1, w_max+1):
            for z in range(z_min-1, z_max+1):
                for y in range(y_min-1, y_max+1):
                    for x in range(x_min-1, x_max+1):
                        neighbors = look_around3(grid,x,y,z,w)
                        #print(f'{x,y,z}: {neighbors}')
                        if 2 <= neighbors <= 3:
                            state = bool(grid.get((x,y,z,w), None))
                            if state or (not state and neighbors == 3):
                                #print(f'{x,y,z}: {state},{neighbors}')
                                new_grid[x,y,z,w] = '#'
                                if not (x_min < x < x_max):
                                    exp_x = True
                                if not (y_min < y < y_max):
                                    exp_y = True
                                if not (z_min < z < z_max):
                                    exp_z = True
                                if not (w_min < w < w_max):
                                    exp_w = True
        if exp_x:
            #print('expanding x')
            x_min -=1
            x_max +=1
        if exp_y:
            #print('expanding y')
            y_min -=1
            y_max +=1
        if exp_z:
            #print('expanding z')
            z_min -=1
            z_max +=1
        if exp_w:
            #print('expanding w')
            w_min -=1
            w_max +=1
        grid = new_grid
        #print_grid3(grid)
    print(len(grid))

part1(grid, width, height)
part2(grid, width, height)