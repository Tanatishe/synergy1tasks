from math import ceil 


class Turtle:
    x = 0
    y = 0
    s = 3

    def __init__(self):
        pass

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_up(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        self.s -= 0
        assert self.s > 0, 'Too slow'

    def count_moves(self, x1, y1):
        steps = ceil((x1 - self.x) / self.s) + ceil((y1 - self.y) / self.s)
        return steps
Leo = Turtle()
print(Leo.count_moves(10,10))
