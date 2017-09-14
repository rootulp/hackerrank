import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    class Cell {

        public int row;
        public int col;

        public Cell(int row, int col) {
            this.row = row;
            this.col = col;
        }

        public String toString() {
            return "Cell[" + Integer.toString(this.row) + "][" + Integer.toString(this.col) + "]";
        }

        @Override public boolean equals(Object other) {
            boolean result = false;
            if (other instanceof Cell) {
                Cell that = (Cell) other;
                result = (this.row == that.row && this.col == that.col);
            }
            return result;
        }

        @Override public int hashCode() {
            return (41 * (41 + this.row) + this.col);
        }
    }

    private int[][] grid;
    private int rows;
    private int cols;

    public Solution(int[][] grid, int rows, int cols) {
        this.grid = grid;
        this.rows = rows;
        this.cols = cols;
    }

    public int largestRegion() {
        int largest = 0;
        for(int row = 0; row < this.rows; row++){
            for(int col = 0; col < this.cols; col++){
                Cell cell = new Cell(row, col);
                if (filled(cell) && computeRegion(cell) > largest) {
                    largest = computeRegion(cell);
                }
            }
        }
        return largest;
    }

    private int computeRegion(Cell cell) {
        Set<Cell> visited = new HashSet<Cell>();
        Stack<Cell> to_visit = new Stack<Cell>();
        to_visit.add(cell);
        while (!to_visit.empty()) {
            Cell currentCell = to_visit.pop();
            visited.add(currentCell);
            for(Cell neighbor : filledNeighbors(currentCell)) {
                if(!visited.contains(neighbor)) {
                    to_visit.add(neighbor);
                }
            }
        }
        return visited.size();
    }

    private Set<Cell> filledNeighbors(Cell cell) {
        Set<Cell> neighbors = new HashSet<Cell>();
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                Cell neighbor = new Cell(cell.row + x, cell.col + y);
                if (isOnGrid(neighbor) && filled(neighbor)) {
                    neighbors.add(neighbor);
                }
            }
        }
        return neighbors;
    }

    private boolean isOnGrid(Cell cell) {
        return cell.row >= 0 && cell.row < this.rows && cell.col >= 0 && cell.col < this.cols;
    }


    private boolean filled(Cell cell) {
        return grid[cell.row][cell.col] == 1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int grid[][] = new int[n][m];
        for(int grid_i=0; grid_i < n; grid_i++){
            for(int grid_j=0; grid_j < m; grid_j++){
                grid[grid_i][grid_j] = in.nextInt();
            }
        }
        Solution s = new Solution(grid, n, m);
        System.out.println(s.largestRegion());
    }
}
