class Block():
    def __init__(self, n:int):
        self.n = n
        self.map = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.answer = [[(i+n*j)%(n**2) for i in range(1, n+1)] for j in range(n)]
        self.blank = [n-1, n-1]
        self.log = []
        
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
        self.log.append(coord)
        
    def distance_answer(self):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                num = self.map[i][j] - 1
                if num == -1:
                    # distance += abs(self.n - 1 - i) + abs(self.n - 1 - j)
                    continue
                distance += abs(num // self.n - i) + abs(num % self.n - j)
        # print([0 if x == y else 1 for map_row, ans_row in zip(self.map, self.answer) for x, y in zip(map_row, ans_row)])
        # return sum([0 if x == y else 1 for map_row, ans_row in zip(self.map, self.answer) for x, y in zip(map_row, ans_row)])
        return distance
    
    def check(self) -> bool:
        # for map_row, ans_row in zip(self.map, self.answer):
        #     for x, y in zip(map_row, ans_row):
        #         print(x, y) 
            
        if all(x == y for map_row, ans_row in zip(self.map, self.answer) for x, y in zip(map_row, ans_row)):
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
            
    def scramble(self, n: int):
        for _ in range(n):
            available = block.available()
            randint = random.randint(0, len(available)-1)
            block.move(available[randint])
    
    def reset_log(self):
        self.log = []
    
if __name__ == "__main__":
    import random, copy
    
    n = 3
    block = Block(n)
    block.scramble(100)
    block.reset_log()
    # block.map = [[1,3,6],[4,0,2],[7,5,8]]
    # block.blank = (1, 1)
    # print(block.map)
    # block.move(6)
    # block.check()
    # print(block.blank)

    block.print()
    # block.print("answer")
    avail_count = len(block.available())
    queue = list(zip(block.available()[:], 
                     [copy.deepcopy(block) for _ in range(avail_count)]))
    visit = []
    answer = None
    while queue:
        tile, object = queue.pop(0)
        if object.check():
            answer = object
            break
        visit.append(object)
        for state in visit:
            if all([x == y for map_row, ans_row in zip(state.map, object.map) for x, y in zip(map_row, ans_row)]):
                continue
        score = len(object.log) + object.distance_answer()
        object.move(tile)
        # print([x[0] for x in queue])
        # object.print()
        # for tile, obj in queue:
        #     obj.print()
        # break
        
        new_score = len(object.log) + object.distance_answer()
        print(tile, score, new_score)
        object.print()
        # if new_score <= score:
        for tile in object.available():
            queue.append((tile, copy.deepcopy(object)))
    # print(object.log)
    if isinstance(answer, Block):
        object.print()
        print([n*x[0] + x[1]+1 for x in object.log])
    else:
        print("Fail!")