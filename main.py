class Block():
    def __init__(self, n):
        self.map = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.answer = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.blank = [n-1, n-1]
        
    def adjacent(self, co1, co2):
        y1, x1 = co1
        y2, x2 = co2
        dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if dis == 1:
            return True
        return False
        
    def move(self, position):
        position -= 1
        # check tile position is valid
        assert 0 <= position and position <= n**2-1
        coord = [position // n, position % n]
        # check tile is adjacent to blank
        assert self.adjacent(self.blank, coord)
        self.map[coord[0]][coord[1]], self.map[self.blank[0]][self.blank[1]] = self.map[self.blank[0]][self.blank[1]], self.map[coord[0]][coord[1]]
        self.blank = coord
        
    def check(self):
        if self.map == self.answer:
            return True
        return False

block = Block(3)
print(block.map)
block.move(6)
print(block.map)
block.check()
