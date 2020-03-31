def main():
    N, K = [int(_) for _ in input().split()]
    i = 1
    while True:
        N_quotient = N // K
        N = N_quotient
        if N != 0:
            i += 1
        else:
            break
    print(i)
main()


# import math
# n,k=map(int,input().split())
# print(int(math.log(n,k))+1)