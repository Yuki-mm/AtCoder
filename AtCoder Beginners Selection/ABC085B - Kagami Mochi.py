def main():
    N = int(input())
    D = []

    for _ in range(N):
        D.append(int(input()))
    
    ans = len(set(D))
    print(ans)
main()