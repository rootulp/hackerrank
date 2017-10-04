class FlippingMatrix:

    def __init__(self, n, matrix):
        self.n = n
        self.matrix = matrix

    def max_sum_of_quadrant(self):
        return sum(self.max_quadrant())

    def max_quadrant(self):
        return [max(self.upper_left_quadrant(row, col),
                    self.upper_right_quadrant(row, col),
                    self.lower_left_quadrant(row, col),
                    self.lower_right_quadrant(row, col))
                for row in range(self.n)
                for col in range(self.n)]

    def upper_left_quadrant(self, row, col):
        return self.matrix[row][col]

    def upper_right_quadrant(self, row, col):
        return self.matrix[row][self.flip(col)]

    def lower_left_quadrant(self, row, col):
        return self.matrix[self.flip(row)][col]

    def lower_right_quadrant(self, row, col):
        return self.matrix[self.flip(row)][self.flip(col)]

    def flip(self, axis):
        return 2 * self.n - 1 - axis


q = int(input().strip())
for _ in range(q):
    n = int(input().strip())
    matrix = []
    for _ in range(2 * n):
        matrix.append(list(map(int, input().strip().split(' '))))
    print(FlippingMatrix(n, matrix).max_sum_of_quadrant())
