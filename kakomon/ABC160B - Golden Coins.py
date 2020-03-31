def main():
    x = int(input())
    
    a = x // 500
    x %= 500

    b = x // 5
    
    ans = 1000 * a + 5 * b
    print(ans)

main()


