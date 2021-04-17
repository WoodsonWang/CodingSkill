"""
@author:Wang Xinsheng
@File:62不同路径.py
@description:62. 不同路径
https://leetcode-cn.com/problems/unique-paths/description/
@time:2021-04-17 22:23
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [[0]*n]*m
        print(len(array))
        count = 1
        for i in range(m):
            for j in range(n):
                array[i][j]=count
                # if i ==0:
                #     array[i][j]=1
                #
                # else:
                #     array[i][j] = array[i-1][j]+array[i][j-1]
                count+=1
        print(array)

if __name__ == '__main__':
    so = Solution()
    so.uniquePaths(5,3)