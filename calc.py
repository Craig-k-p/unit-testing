'''Practice using the unittest module'''


class Shape():
    def __init__(self, *args):
        '''Accepts any number of tuples containing an x and y coordinate.
        not_square = Shape((1,2), (3,4), (5,6), (7,8))'''

        # A tuple of tuples with x,y coordinates
        self.points = args
        self.x_points = [p[0] for p in args]
        self.y_points = [p[1] for p in args]

        # The centered or average x and y position
        self.centered_pos_x = sum(self.x_points) / len(self.x_points)
        self.centered_pos_y = sum(self.y_points) / len(self.y_points)

    def __str__(self):
        if len(self.points) == 1:
            return f'A point centered at position {(self.relative_pos_x, self.relative_pos_y)}.'
        elif len(self.points) == 2:
            return f'A line centered at position {(self.relative_pos_x, self.relative_pos_y)}.'
        else:
            return f'{len(self.points)}-sided Shape centered at position {(self.relative_pos_x, self.relative_pos_y)}.'

    def __eq__(self, other):
        '''Return True if the shapes have the same coordinates'''
        if isinstance(other, tuple):
            return self.points.sort() == other.points.sort()

    def __add__(self, other):
        '''Transform the shape'''
        if isinstance(other, Shape):
            if len(self.points) == len(other.points):
                new_points = []
                # New sorted tuples
                s, o = self.points.sorted(), other.points.sorted()
                for i in range(len(s)):
                    new_points.append(
                        # Append tuples like (x1 + x2, y1 + y2) to the new_points list
                        (s[i][0] + o[i][0], s[i][1] + o[i][1])
                    )
                return new_points

            else:
                return None

    def __sub__(self, other):
        '''Get the distance between the center point of each shape'''
        if isinstance(other, Shape):
            return (self.relative_pos_x - other.relative_pos_x, self.relative_pos_y - other.relative_pos_y)


square = Shape((1, 1), (1, 2), (2, 2), (2, 1))
triangle = Shape((4, 4), (6, 4), (5, 6))
square2 = Shape((5, 1), (5, 2), (6, 2), (6, 1))

print(square)
print(triangle)
print(square2)
