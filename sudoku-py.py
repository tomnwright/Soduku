import random

class s9Grid:
    def __init__(self):
        self.grid = [[' ' for j in range(9)] for i in range(9)]

    def __iter__(self):
        return [row for row in self.grid]

    def __getitem__(self, key):
        '''key = (x,y,)'''
        return self.grid[key[1]][key[0]]
    def __setitem__(self, key, value):
        self.grid[key[1]][key[0]] = value
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
                if j == ' ':
                    return False
        return True

    def getCell (self, i):
        cell = []
        for j in range(9):
            #elements
            x =  3 * (i % 3) + (j % 3)
            y =  3 * (i // 3) + (j // 3)

            cell.append(self[x,y])
        return cell
    
    def getRow (self, row):

        return self.grid[row]
    
    def getColumn (self, column):

        return [row[column] for row in self.grid]

    def CanGo (self, key, value):
        b1 = value in self.getCell(s9Grid.cellNumber(*key))
        b2 = value in self.getColumn(key[0])
        b3 = value in self.getRow(key[1])
        return not (b1 or b2 or b3)

    @staticmethod
    def cellNumber(x, y):
        return 3 * (y // 3) + (x // 3)
        #j = 3 * (y % 3) + (x % 3), see getCell


def testKey(grid, key):
    numbers = list(range(1,10))

    while (numbers):

        val = random.choice(numbers)
        numbers.remove(val)

        if grid.CanGo(key,val):
            return val

    return None


#define all keys
keysRaw = []
for i in range(9):
    for j in range(9):
        k = (i,j,)
        keysRaw.append(k)

count = 0
best = 0
while True:

    grid = s9Grid()
    keys = keysRaw.copy()
     
    buffer = []
    success_count = 0
    while not grid.solved():
        key = random.choice(keys)
        if key in buffer:
            continue

        test = testKey(grid,key)
        if (test):
            
            success_count += 1
            grid[key] = test
            buffer = []
            keys.remove(key)

        else:

            buffer.append(key)
            if set(buffer) == set(keys):
                break
    count += 1
    print(grid, end = '\n\n\n')
    
    
    if grid.solved() or count > 50:
        break
print('SOLVED')
input()