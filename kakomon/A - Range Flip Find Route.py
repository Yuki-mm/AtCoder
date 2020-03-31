
def ods():
    s = input()
    slist = []
    slist.append(s.split())
    for i in range(0, len(s), 2):
        print(slist[i])

ods()