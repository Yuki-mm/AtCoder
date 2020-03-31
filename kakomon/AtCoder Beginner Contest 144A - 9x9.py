def main():
    A, B = map(int, input().split())
    if A < 10 and B < 10:
        p = A * B
        print(p)
    else:
        print(-1)
main()