class InsertionSort(object):

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        unsorted = self.arr[-1]
        pointer_i = len(self.arr) - 2
        while(unsorted < self.arr[pointer_i] and pointer_i >= 0):
            self.arr[pointer_i + 1] = self.arr[pointer_i]
            self.print_arr()
            pointer_i -= 1
        self.arr[pointer_i + 1] = unsorted
        self.print_arr()

    def print_arr(self):
        print(" ".join(list(map(str, self.arr))))

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
InsertionSort(arr).sort()