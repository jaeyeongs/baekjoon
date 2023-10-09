N = int(input())
s = 666
count = 0

while True:
    if '666' in str(s):
        count += 1

    if count == N:
        print(s)
        break

    s += 1