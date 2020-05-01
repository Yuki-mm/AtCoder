import sys

def main():
    n, k = [int(_) for _ in input().split()]
    
    m = abs(n - n // k * k)
    while True:
        ans = abs(m - k)
        if m <= ans:
            print(m)
            sys.exit()
        m = abs(m - k)
main()