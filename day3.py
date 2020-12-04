with open('input3.txt') as f:
    grid = [list(g) for g in f.read().split()]


def hit_trees(g, xx, yy):
    x = y = all_the_trees_I_hit = 0
    height = len(g)
    width = len(g[0])
    while y < height:
        what_is_this = g[y % height][x % width]
        if what_is_this == '#':
            all_the_trees_I_hit += 1
        x += xx
        y += yy
    return all_the_trees_I_hit
a = hit_trees(grid, 1, 1)
b = hit_trees(grid, 3, 1)
c = hit_trees(grid, 5, 1)
d = hit_trees(grid, 7, 1)
e = hit_trees(grid, 1, 2)
print(b)
print(a*b*c*d*e)