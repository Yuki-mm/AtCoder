import math
def main():
    N = int(input())
    l = [int(_) for _ in input().split()]
    count_list = [0] * N
    for i in l:
        index = i - 1
        count_list[index] += 1

    for out in count_list:
        print(out)
main()