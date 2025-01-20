class Block():
    def __init__(self, n):
        self.n = n
        self.map = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.answer = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.blank = [n-1, n-1]
        
    def distance(self, co1, co2):
        y1, x1 = co1
        y2, x2 = co2
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    def adjacent(self, co1, co2):
        dis = self.distance(co1, co2)
        if dis == 1:
            return True
        return False

    def available(self):
        y, x = self.blank
        result = []
        for tile in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
            position = self.n * tile[0] + tile[1]
            if 0 <= position and position < self.n**2:
                result.append(tile)
        return result
        
    def move(self, target: int | list[int]) -> None:
        if isinstance(target, int):
            position = target - 1
        elif isinstance(target, list):
            position = self.n * target[0] + target[1]

        # check tile position is valid
        assert 0 <= position < self.n**2
        coord = [position // self.n, position % self.n]
        # check tile is adjacent to blank
        assert self.adjacent(self.blank, coord)
        self.map[coord[0]][coord[1]], self.map[self.blank[0]][self.blank[1]] = self.map[self.blank[0]][self.blank[1]], self.map[coord[0]][coord[1]]
        self.blank = coord
            
        
    def check(self):
        if self.map == self.answer:
            return True
        return False

if __name__ == "__main__":
    block = Block(3)
    print(block.map)
    # block.move(6)
    # block.check()
    print(block.blank)
    available = block.available()
    block.move(available[1])
    print(block.map)
