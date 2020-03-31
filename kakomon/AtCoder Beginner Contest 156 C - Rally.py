def main():
    N = int(input())
    xlist = list(map(int, input().split()))
    x_min = min(xlist)
    x_max = max(xlist)
    min_sum_value = 10**15
    
    for p in range(100):
        c = 0
        for i in xlist:
            c += (i - p) ** 2
        if min_sum_value > c:
            min_sum_value = c
    print(min_sum_value)

main()


