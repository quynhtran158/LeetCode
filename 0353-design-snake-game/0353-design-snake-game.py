class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([0, 0])
        self.width = width
        self.height = height
        self.set = set()
        self.set.add((0, 0))
        

    def move(self, direction: str) -> int:
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)