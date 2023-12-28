a = int(input())
d = {}
for i in range(a):
    x = input().split('||')
    # print(x)
    if x[0] not in d:
        d[x[0]] = set()
    d[x[0]].add(x[3])

ansd = sorted(d.items(), key=lambda t: (-len(t[1]), t[0]))
print(ansd[0][0])
