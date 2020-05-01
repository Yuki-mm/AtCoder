from math import gcd
from functools import reduce

# def gcd(*numbers):
#     r = reduce(math.gcd, numbers)
#     return r

def main():
    K = int(input())
    g = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                g += gcd(gcd(i, j), k)         
    print(g)
main()

# from itertools import combinations

# import itertools
# import math
 
# n = int(input())
 
# ans = 0
# ans1 = 0
# ans2 = 0
# ans3 = 0
# for i, j, k in itertools.combinations(range(1, n+1), 3):
#     ans1 += math.gcd(math.gcd(i, j), k)*6
 
# for i, j in itertools.combinations(range(1, n+1), 2):
#     ans2 += math.gcd(i, j) * 3 * 2
 
# ans3 += (1 + n)*n//2
 
# # print(ans1, ans2, ans3)
# print(ans1+ans2+ans3)