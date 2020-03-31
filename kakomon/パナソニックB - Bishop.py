import sys
import math

def main():
    H, W = [int(_) for _ in input().split()]
    if H == 1 or W == 1:
        m = 1
        print(int(m))
        sys.exit()
        
    elif H % 2 == 1 and W % 2 == 1:
        m = (H * W) // 2 + 1
    else:
        m = (H * W) // 2
    print(int(m))
main()