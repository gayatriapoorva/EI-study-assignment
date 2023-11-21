from enum import Enum

# Command Pattern
class Command:
    def execute(self, rover):
        pass

class M(Command):
    def execute(self, rover):
        rover.move()

class L(Command):
    def execute(self, rover):
        rover.turn_left()

class R(Command):
    def execute(self, rover):
        rover.turn_right()

# Composite Pattern
class GridComponent:
    def is_obstacle(self, x, y):
        pass

class Obstacle(GridComponent):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_obstacle(self, x, y):
        return self.x == x and self.y == y

class Grid(GridComponent):
    def __init__(self, size, obstacles):
        self.size = size
        self.obstacles = obstacles

    def is_obstacle(self, x, y):
        return any(obstacle.is_obstacle(x, y) for obstacle in self.obstacles)

# Rover Class
class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move(self):
        new_x, new_y = self.calculate_new_position()
        if not self.grid.is_obstacle(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        directions = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = directions[self.direction]

    def turn_right(self):
        directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = directions[self.direction]

    def calculate_new_position(self):
        x, y = self.x, self.y
        if self.direction == 'N':
            y += 1
        elif self.direction == 'S':
            y -= 1
        elif self.direction == 'E':
            x += 1
        elif self.direction == 'W':
            x -= 1
        return x, y

    def status_report(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."

    def final_position(self):
        return f"Final Position: ({self.x}, {self.y}, {self.direction})"

if __name__ == "__main__":
    obstacles = [Obstacle(2, 2), Obstacle(3, 5)]
    grid = Grid(size=(10, 10), obstacles=obstacles)
    rover = Rover(x=0, y=0, direction='N', grid=grid)

    commands = [M(), M(), R(), M(), L(), M(), M(), R()]

    for command in commands:
        command.execute(rover)

    print(rover.final_position())
    print(rover.status_report())
