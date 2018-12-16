class Grid(object):

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def largest_region(self):
        return max([self.region_size(row, col)
                    for row in range(self.rows)
                    for col in range(self.cols)])

    def region_size(self, row, col):
        if not self.filled_cell(row, col):
            return 0
        return self.bfs_for_region_size(row, col)

    def bfs_for_region_size(self, row, col):
        visited = set()
        to_visit = [(row, col)]
        while to_visit:
            row, col = to_visit.pop()
            if (row, col) not in visited:
                visited.add((row, col))
                to_visit.extend(self.filled_neighbors(row, col))
        return len(visited)

    def filled_neighbors(self, row, col):
        return list(filter(lambda cell: self.filled_cell(cell[0], cell[1]),
                           self.neighbors(row, col)))

    def neighbors(self, row, col):
        return list(filter(lambda cell:
                           self.row_in_grid(cell[0]) and
                           self.col_in_grid(cell[1]),
                           self.potential_neighbors(row, col)))

    def potential_neighbors(self, row, col):
        return [(row + row_delta, col + col_delta)
                for row_delta in range(-1, 2)
                for col_delta in range(-1, 2)]

    def filled_cell(self, row, col):
        return self.grid[row][col] == 1

    def row_in_grid(self, row):
        return 0 <= row < self.rows

    def col_in_grid(self, col):
        return 0 <= col < self.cols


rows = int(input().strip())
cols = int(input().strip())
grid = [list(map(int, input().strip().split(" "))) for _ in range(rows)]
print(Grid(grid).largest_region())
