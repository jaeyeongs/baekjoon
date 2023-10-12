import sys

n = int(sys.stdin.readline())
d = dict()

for i in range(n):
    name, commute = sys.stdin.readline().split()
    if commute == 'enter':
        d[name] = 'enter'
    else:
        del d[name]

s = sorted(d.keys(), reverse=True)

for i in s:
    print(i)