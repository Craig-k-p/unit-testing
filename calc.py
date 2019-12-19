'''Practice using the unittest module'''


class Shape():
    def __init__(self, *args):
        self.points = args
        self.x_points = [p[0] for p in args]
        self.y_points = [p[1] for p in args]
        self.relative_pos_x = sum(self.x_points) / len(self.x_points)
        self.relative_pos_y = sum(self.y_points) / len(self.y_points)

    def __str__(self):
        if len(self.points) == 1:
            return f'A point centered at position {(self.relative_pos_x, self.relative_pos_y)}.'
        elif len(self.points) == 2:
            return f'A line centered at position {(self.relative_pos_x, self.relative_pos_y)}.'
        else:
            return f'{len(self.points)}-sided Shape centered at position {(self.relative_pos_x, self.relative_pos_y)}.'

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.points.sort() == other.points.sort()

    def __add__(self, other):
        if isinstance(other, Shape):
            if len(self.points) == len(other.points):
                new_points = []
                for i in range(len(self.points)):
                    new_points.append(
                        (self.points[i][0] + other.points[i][0], self.points[i][1] + other.points[i][1])
                    )
                return new_points

            else:
                return (self.relative_pos_x + other.relative_pos_x, self.relative_pos_y + other.relative_pos_y)\



square = Shape((1, 1), (1, 2), (2, 2), (2, 1))
triangle = Shape((4, 4), (6, 4), (5, 6))
square2 = Shape((5, 1), (5, 2), (6, 2), (6, 1))

print(square, triangle, square2)
