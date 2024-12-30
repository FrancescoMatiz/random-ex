import random

class Prob:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def __init__(self) -> None:
        self.position : tuple[int, int] = (0, 0)
        self.step = 0
    

    def _next_position(self):
        r = random.randint(0, 3)
        dir = Prob.DIRS[r]
        self.position = (self.position[0] + dir[0], self.position[1] + dir[1])
        self.step += 1

    def __iter__(self):
        return self

    def __next__(self):
        self._next_position()
        return (self.position, (self.position[0] * self.position[0] + self.position[1] * self.position[1]) / self.step)




prob = Prob()
for p in prob:
    print(p)



