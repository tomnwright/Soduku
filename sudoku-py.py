import random

class s9Grid:
    def __init__(self):
        self.grid = [[i * j for j in range(9)] for i in range(9)]

    def __iter__(self):
        return [row for row in self.grid]

    def __getitem__(self, key):
        return self.grid[key[0]][key[1]]
    def __setitem__(self, key, value):
        self.grid[key[0]][key[1]] = value
    def __str__(self):
        out = ''
        
        for e1,i in enumerate(self.grid):
            if e1 in [3, 6]:
                out += '-' * 31
                out += '\n'
            for e2,j in enumerate(i):
                if e2 in [3, 6]:
                    out += '|  '
                out += str(j)
                out += '  '
            out += '\n'

        return out

    def solved (self):
        for i in self.grid:
            for j in i:
                if j == 0:
                    return False
        return True

    def sudokuFormat (self):
        
        out = []
        for i in range(9):
            #cells
            cell = []
            for j in range(9):
                #elements
                y =  3 * (i // 3)  +  3 * (j // 3)
                x =  3 * (i % 3)   + 3 * (j // 3)
                cell += self[y,x,]
            out += cell
        return cell
        


grid = s9Grid()

keys = [[(i,j,) for j in range(9)] for i in range(9)]
'''
while not grid.solved():
    pass
'''
print(grid)
print(grid.sudokuFormat())