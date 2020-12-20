import re
import numpy
with open('input20.txt') as f:
    tiles_raw = f.read().split('\n\n')
    tiles = {}
    for t in tiles_raw:
        tid, tile = t.split(':')
        tid = int(tid.replace('Tile ',''))
        tile = [list(t) for t in tile.strip().split('\n')]
        tiles[tid] = tile

def read_side(tile, side):
    output = None
    if side == 0:
        output = ''.join(tile[0])
    elif side == 1:
        output = ''.join(t[-1] for t in tile)
    elif side == 2:
        output = ''.join(tile[-1][::-1])
    elif side == 3:
        output = ''.join(t[0] for t in tile[::-1])
    return output

def print_tile(tiledata, rotation = 0, flip = False):
    tile = [[t for t in tilerow] for tilerow in tiledata]
    if flip:
        tile = numpy.fliplr(tile)
    tile = numpy.rot90(tile, -rotation)
    return [''.join(row) for row in tile]

def match_tiles(tilea, tileb):
    # returns whether it is a match
    # which side is matched from tilea and tileb
    # and whether or not it is flipped
    for a in range(4):
        sidea = read_side(tilea, a)
        for b in range(4):
            sideb = read_side(tileb, b)
            if sidea == sideb:
                return True, a, b, True
            elif sidea == sideb[::-1]:
                # [(b + 2) % 4 if b % 2 == 1 else b] is the flipped coordinate.
                # replaces 1 (right) with 3 (left) and vice versa.
                return True, a, b, False
    return False, a, b, False


tiles_counter = {k:0 for k, v in tiles.items()}
adj_mtx = dict()
for ka,va in tiles.items():
    for kb,vb in tiles.items():
        if ka == kb:
            continue
        match, a, b, flipped = match_tiles(va,vb)
        if match:
            #print(f'tile {ka} on side {a} matches tile {kb} on side {b} {"with flipping" if flipped else ""}')
            #print(print_tile(va))
            #print('\n')
            #print(print_tile(vb,b-a-2, flipped))
            #print('\n')
            adj_mtx[ka,kb] = adj_mtx[kb,ka] = a, b, flipped
            tiles_counter[ka] += 1
#print(tiles_counter)
b = [k for k,v in tiles_counter.items() if v == 2]
prod = 1
for bb in b:
    prod *= bb
print(prod)
'''
for y in tiles.keys():
    row = []
    for x in tiles.keys():
        spot = adj_mtx.get((x,y),None)
        row.append('x' if spot else '.')
    print(''.join(row))
'''
def get_free_neighbors(board):
    spots = set()
    to_check = [
        (0,-1),
        (1,0),
        (0,1),
        (-1,0)]
    for (x, y), t in board.items():
        for ox, oy in to_check:
            if board.get((x+ox,y+oy), None) is None:
                spots.add((x+ox,y+oy))
    return list(spots)

def draw_board(board, border = True):
    y_range = [y for x,y in board.keys()]
    x_range = [x for x,y in board.keys()]
    y_min, y_max = min(y_range), max(y_range)
    x_min, x_max = min(x_range), max(x_range)
    output = []
    for y in range(y_min,y_max+1):
        rows = []
        for i in range(10) if border else range(1,9):
            subrows = []
            for x in range(x_min,x_max+1):
                spot = board.get((x,y), None)
                line = (spot[3][i] if border else spot[3][i][1:-1]) if spot else (' '*10 if border else ' '*8)
                subrows.append(line)
            rows.append(''.join(subrows))
        output.append('\n'.join(rows))
    return '\n'.join(output)

pieces = list(tiles.keys())
board = dict()
first_piece = pieces.pop(0)
rotation = 2
flip = True
board[0,0] = (first_piece, rotation, flip, print_tile(tiles[first_piece], rotation, flip))
to_check = [
                (0,-1),
                (1,0),
                (0,1),
                (-1,0)]

while len(pieces):
    old_board = {k:v for k,v in board.items()}
    for (x,y), (piece, rotation, flipped, tile) in old_board.items():
        
        possible = [b for a, b in adj_mtx.keys() if a == piece]

        for p in possible:
            if p in pieces:
                T, sidea, sideb, flip = match_tiles(tile, tiles[p])
                ox,oy = to_check[(sidea)%4]
                #print(x+ox, y+oy, piece, p, sidea, sideb, flipped, flip)

                if flip:
                    sideb = (sideb + 2) % 4 if sideb % 2 == 1 else sideb

                rot = 2 + (sidea-sideb)
                tile2 = print_tile(tiles[p], rot, flip)
                board[x+ox,y+oy] = p, rot, flip, tile2
                pieces.remove(p)


    '''
    y_range = [y for x,y in board.keys()]
    x_range = [x for x,y in board.keys()]
    y_min, y_max = min(y_range), max(y_range)
    x_min, x_max = min(x_range), max(x_range)
    for y in range(y_min,y_max+1):
        a = []
        for x in range(x_min,x_max+1):
            spot = board.get((x,y), None)
            spot = str(spot[0]) if spot else '    '
            a.append(spot)
        ' '.join(a)
        print(a)
    '''

    #print(draw_board(board))
    #print('\n')
    #input()
view_camera = draw_board(board, False)
print(view_camera)

camera = view_camera.split('\n')

snek = [
'00000000000000000010',
'10000110000110000111',
'01001001001001001000'
]
snek = [[int(s) for s in row] for row in snek]
flip_snek = numpy.fliplr(snek)
sneks = [snek,flip_snek]
for r in range(1,4):
    sneks.append(numpy.rot90(snek,r))
    sneks.append(numpy.rot90(flip_snek,r))

def match_snek(x,y,snek):
    #section = []
    snek_found = True
    for sy in range(len(snek)):
        #row = []
        for sx in range(len(snek[0])):
            #if x == 2 and y == 2:
            #    print(camera[y+sy][x+sx], snek[sy][sx], sx, sy)
            #    row.append(camera[y+sy][x+sx])
            if snek[sy][sx] == 0:
                continue
            elif camera[y+sy][x+sx] == '.':
                return False
        #section.append(''.join(row))
    #if x == 2 and y == 2:
    #    print('\n'.join(''.join(str(s) for s in row) for row in snek))
    #    print('\n'.join(section))
    if snek_found:
        return True
    return False
snek_counter = 0
for snek in sneks:
    #print(len(camera),len(camera[0]))
    #print(len(snek),len(snek[0]))
    y_range = range(0,len(camera)-len(snek)+1)
    x_range = range(0,len(camera[0])-len(snek[0])+1)
    #print(list(y_range))
    #print(list(x_range))
    for y in y_range:
        for x in x_range:
            snek_found = match_snek(x,y,snek)
            if snek_found:
                snek_counter += 1
print(sum(1 for c in view_camera if c == '#') - snek_counter * 15)