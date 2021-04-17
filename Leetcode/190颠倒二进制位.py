"""
@author:Wang Xinsheng
@File:190颠倒二进制位.py
@description:...
@time:2021-03-29 19:30
"""

def reverseBits(n:int)->int:
    res = 0
    for i in range(4):
        res = (res<<1)|(n&1)
        n>>=1
    print(bin(res))



if __name__ == '__main__':
    n = 0b1010

    reverseBits(n)
