
def main():
    N, M = [int(_) for _ in input().split()]
    slist = list(map(int, input().split()))
    sort_list = sorted(slist)
    thr = sum(sort_list) / (4 * M)
    
    cnt = 0
    for i in sort_list:
        if i >= thr:
            cnt += 1

    if cnt >= M:
        print("Yes")
    else:
        print("No")

main()