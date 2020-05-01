import math
def main():
    N, M = map(int, input().split())
    l = [int(_) for _ in input().split()]
    summer_vacation_day_count = sum(l)
    if summer_vacation_day_count <= N:
        out = N - summer_vacation_day_count
    else:
        out = -1
    print(out)
main()