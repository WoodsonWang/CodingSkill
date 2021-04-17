"""
@author:Wang Xinsheng
@File:59螺旋矩阵II.py
@description:...
@time:2021-03-27 20:31
"""

def generate(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    left=up=0
    right=below=n-1
    num = 1
    while(num<=n**2):

        # 从左到右
        for i in range(left,right+1):
            mat[up][i] = num
            num+=1
            print(num)
        up+=1
        # 从上到下
        for i in range(up,below+1):
            print(i)
            mat[i][right]=num
            num+=1
        right-=1
        # 从右到左
        for i in range(right,left-1,-1):
            mat[below][i]=num
            num+=1
        below-=1

        # 从下到上
        for i in range(below,up-1,-1):
            mat[i][left] = num
            num+=1
        left+=1

    print(mat)


if __name__ == '__main__':
   generate(4)

