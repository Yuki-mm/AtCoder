
def main():
    N = int(input())
    keihin_l = []
    
    for _ in range(N):
        s = input()
        keihin_l.append(s)

    delete_duplicate_list = set(keihin_l)
    out = len(list(delete_duplicate_list))
    print(out)
main()