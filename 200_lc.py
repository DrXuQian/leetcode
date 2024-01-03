from typing import List


class Solution:
    def find_neighbors(self, i, j, grid, visited):
        visited.add((i, j))
        if grid[i][j] == "0":
            return visited
        if i > 0 and (i - 1, j) not in visited:
            self.find_neighbors(i - 1, j, grid, visited)
        if j > 0 and (i, j - 1) not in visited:
            self.find_neighbors(i, j - 1, grid, visited)
        if i < len(grid) - 1 and (i + 1, j) not in visited:
            self.find_neighbors(i + 1, j, grid, visited)
        if j < len(grid[0]) - 1 and (i, j + 1) not in visited:
            self.find_neighbors(i, j + 1, grid, visited)
        return


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ret = 0
        for i, c in enumerate(grid):
            for j, r in enumerate(c):
                if (i, j) in visited:
                    continue
                self.find_neighbors(i, j, grid, visited)
                if r == "1":
                    ret += 1
        return ret





grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))