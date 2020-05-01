
def main():
    S, W = map(int, input().split())
    if W >= S:
        out = 'unsafe'
    else:
        out = 'safe'
    print(out)
main()