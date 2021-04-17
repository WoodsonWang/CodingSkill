"""
@author:Wang Xinsheng
@File:64最小路径和.py
@description:...
@time:2021-04-17 0:55
"""
class Solution:
    def minPathSum(self, grid: int) -> int:
        rows = len(grid)
        colums = len(grid[0])
        for r in range(rows):
            for c in range(colums):
                if r == 0:
                    if c == 0:
                        pass
                    else:
                        grid[r][c] += grid[r][c-1]
                else:
                    if c == 0:
                        grid[r][c] += grid[r-1][c]
                    else:
                        grid[r][c] += min(grid[r-1][c],grid[r][c-1])
        return grid[-1][-1]



if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    so = Solution()
    result = so.minPathSum(grid)
    print(result)