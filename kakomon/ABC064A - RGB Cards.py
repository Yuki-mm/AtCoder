import sys

def main():
    r, g, b = map(int, input().split())
    # num = int(r + g + b)
    x = 10 * g + b
    if x%4==0:
        print('YES')
    else:
        print('NO')

main()


# import sys

# def main():
#     N = int(input())
#     A = int(input())
#     x = N % 500
#     if x%A==0:
#         print('Yes')
#     else:
#         print('No')

# main()
# 

# import math
# def main():
#     a, b = map(int, input().split())
#     x = (a + b ) / 2
#     x = math.ceil(x)
#     print(x)
# main()

import math
# def main():
#     S = input()
#     cnt = 0
#     for i in range(3):
#         if S[i]=='o':
#             cnt += 1
#     ans = 700 + cnt * 100
#     print(ans)
# main()