"""
@author:Wang Xinsheng
@File:70爬楼梯.py
@description:...
@time:2021-04-11 2:02
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n>=2:
            one = 1
            two = 2
            for i in range(3,n+1):
                last = one+two
                one = two
                two = last
        return two



if __name__ == '__main__':
    so = Solution()
    result = so.climbStairs(5)
    print(result)