def main():
    N = int(input())
    a = N // 100
    b = (N % 100) // 10
    c = N % 10
    l = [a, b, c]
    if 7 in l:
        output = 'Yes'
    else:
        output = 'No'
    print(output)
 
main()