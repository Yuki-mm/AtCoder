
def main():
    A, B, C, D = map(int, input().split())
    
    takahashi_hp = A
    aoki_hp = C
    
    while True:
        aoki_hp = aoki_hp - B
        if takahashi_hp <= 0:
            out = 'No'
            break

        takahashi_hp = takahashi_hp - D   
        if aoki_hp <= 0:
            out = 'Yes'
            break
    print(out)
main()