class Block():
    def __init__(self, n:int):
        self.n = n
        self.map = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.answer = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.blank = [n-1, n-1]
        
    def distance(self, co1: list, co2: list) -> float:
        y1, x1 = co1
        y2, x2 = co2
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    
    def adjacent(self, co1: list, co2: list) -> bool:
        dis = self.distance(co1, co2)
        if dis == 1:
            return True
        return False

    def available(self) -> list[list]:
        y, x = self.blank
        result = []
        for tile in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
            if 0 <= tile[0] < self.n and 0 <= tile[1] < self.n:
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
    
    def check(self) -> bool:
        if self.map == self.answer:
            return True
        return False
    
    def print(self, type="map"):
        if type == "map":
            target = self.map
        elif type == "answer":
            target = self.answer
        for i in range(self.n):
            for j in range(self.n):
                print(target[i][j], end = " ")
            print()
            
    def scramble(self, n: int) -> list:
        order = []
        for _ in range(n):
            available = block.available()
            randint = random.randint(0, len(available)-1)
            block.move(available[randint])
            order.append(available[randint])
        return order
    

if __name__ == "__main__":
    import random
    
    def test(map, blank: list[int], target: int | list[int]) -> list[list[int]]:
        n = len(map)
        if isinstance(target, int):
            position = target - 1
        elif isinstance(target, list):
            position = n * target[0] + target[1]

        # check tile position is valid
        assert 0 <= position < n**2
        coord = [position // n, position % n]
        
        # [:] make new object!
        result = [row[:] for row in map]
        # result = [row.copy() for row in map]
        result[coord[0]][coord[1]], result[blank[0]][blank[1]] = result[blank[0]][blank[1]], result[coord[0]][coord[1]]
        return result, coord
    
    def distance_answer(map):
        n = len(map)
        distance = 0
        for i in range(n):
            for j in range(n):
                num = map[i][j] - 1
                if num == -1:
                    distance += abs(n - 1 - i) + abs(n - 1 - j)
                else:
                    distance += abs(num // n - i) + abs(num % n - j)
        return distance
    
    block = Block(3)
    block.map = [[1,3,6],[4,0,2],[7,5,8]]
    block.blank = (1, 1)
    # print(block.map)
    # block.move(6)
    # block.check()
    # print(block.blank)

    block.print()
    # block.print("answer")
    avail_count = len(block.available())
    queue = list(zip(block.available()[:], 
                     [block.map[:][:] for _ in range(avail_count)], 
                     [block.blank[:] for _ in range(avail_count)],
                     [distance_answer(block.map) for _ in range(avail_count)]))
    while queue:
        tile, map, blank, score = queue.pop(0)
        new_map, new_blank = test(map, blank, tile)
        new_score = distance_answer(new_map)
        if new_score < score:
            queue.append()
    
    # print(block.distance_answer())
