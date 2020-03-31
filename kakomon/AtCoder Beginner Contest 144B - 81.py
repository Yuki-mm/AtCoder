import sys

def main():
    n = int(input())
    for i in range(1, 10, 1):
        if 1 <= n//i <= 9 and (n/i).is_integer():
            print('Yes')
            sys.exit()
    print('No')

main()