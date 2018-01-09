class Direction:
    SOUTH = 's'
    WEST = 'a'
    EAST = 'd'
    NORTH = 'w'


class Mainsymbol:
    def __init__(self, symbol, startx=0, starty=0, velx=1, vely=1, trace='*'):
        self.symbol = symbol
        self.x = startx
        self.y = starty
        self.velx = velx
        self.vely = vely
        self.trace = trace

    def move(self, direction):
        if direction == Direction.SOUTH:
            self.y += self.vely
        elif direction == Direction.NORTH:
            self.y -= self.vely
        elif direction == Direction.EAST:
            self.x += self.velx
        elif direction == Direction.WEST:
            self.x -= self.velx
