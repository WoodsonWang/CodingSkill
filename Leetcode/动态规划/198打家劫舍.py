"""
@author:Wang Xinsheng
@File:198打家劫舍.py
@description:...
@time:2021-04-10 23:55
"""
class Solution:
    def rob(self, nums: [[int]]) -> int:
        size = len(nums)
        if size==0:
            return 0
        dp = [0] * size
        dp[0] = nums[0]
        if size>=2:
            dp[1] = max(dp[0],nums[1])
            for i in range(2,size):
                dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[size-1]

if __name__ == '__main__':
    a = [1,2,3,1]
    so = Solution()
    result = so.rob(a)
    print(result)