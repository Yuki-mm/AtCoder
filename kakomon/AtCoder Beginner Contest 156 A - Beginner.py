def main():
    K = 0
    N, R = [int(_) for _ in input().split()]
    if N >= 10:
        K = R
    else:
        K = R + 100 * (10 - N) 
    print(K)
main()