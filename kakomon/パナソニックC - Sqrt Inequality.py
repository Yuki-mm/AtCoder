import sys
import math
from decimal import Decimal

def main():
    a, b, c = [int(_) for _ in input().split()]

    a_sq = Decimal(a).sqrt()
    b_sq = Decimal(b).sqrt()
    c_sq = Decimal(c).sqrt()

    if a_sq + b_sq < c_sq:
        print("Yes")
    else:
        print("No")
main()