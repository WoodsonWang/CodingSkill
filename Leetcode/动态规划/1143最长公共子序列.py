"""
@author:Wang Xinsheng
@File:1143最长公共子序列.py
@description:...
@time:2021-04-11 21:46
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        up_value = [0]*(n+1)
        for text1_index in range(m):
            current_value = [0]*(n+1)
            for text2_index in range(n):
                if text1[text1_index] == text2[text2_index]:
                    current_value[text2_index+1] = up_value[text2_index]+1
                    # up_value[text2_index] = left_value
                else:
                    current_value[text2_index+1] = max(up_value[text2_index+1],current_value[text2_index])
            up_value = current_value
        return up_value[-1]

if __name__ == '__main__':
    so = Solution()
    result = so.longestCommonSubsequence('abcba','abcbcba')
    print(result)
