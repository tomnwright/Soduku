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

        
    def linear(self):
        out = []
        for i in self.grid:
            for j in i:
                out.append(j)
        return out

    def MustGo(self):

        for c in range(9): #9 cells
            cell = self.getCell(c)

            for n in range(1,10): #each number
                if n in cell:
                    continue
                
                spaces = []
                for key in self.getCellKeys(c):
                    if self[key] == 0:
                        spaces.append(key)
                
                possible = []
                for s in spaces:
                    inColumn = n in self.getColumn(s[0])
                    inRow = n in self.getRow(s[1])
                    if not (inColumn or inRow):
                        possible.append(s)

                if len(possible) == 1:
                    foundKey = possible[0]
                    self.grid[foundKey] = n
                    return foundKey
        return
                    

                

                

    @staticmethod
    def getCellKeys (i):
        keys = []
        for j in range(9):
            #elements
            x =  3 * (i % 3) + (j % 3)
            y =  3 * (i // 3) + (j // 3)

            keys.append((x,y,))
        return keys

    @staticmethod
    def cellNumber(x, y):
        return s9Grid.XYtocell(x,y,)[0]

    @staticmethod
    def XYtocell(x,y,):
        i = 3 * (y // 3) + (x // 3)
        j = 3 * (y % 3) + (x % 3)
        return (i,j,)
    @staticmethod
    def celltoXY(i, j):
        x =  3 * (i % 3) + (j % 3)
        y =  3 * (i // 3) + (j // 3)
        return (x,y,)




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

with open('log.txt', 'a') as logFile:

    count = 0
    best = 0
    while True:

        grid = s9Grid()
        keys = keysRaw.copy()
        
        buffer = []
        success_count = 0
        while not grid.solved():
            foundMust = grid.MustGo()
            if foundMust:
                print('FOUND MUST')
                success_count += 1
                buffer = []
                keys.remove(foundMust)
                continue
            else:
                print('didnt')

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
        logFile.write(str(success_count) + '\n')

        print('Grid no.{}, {} spaces filled'.format(count, success_count))


            

        
        
        if grid.solved():
            break

print('SOLVED')
input()