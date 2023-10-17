import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "1":
        d.appendleft(int(command[1]))

    elif command[0] == "2":
        d.append(int(command[1]))

    elif command[0] == "3":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())

    elif command[0] == "4":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif command[0] == "5":
        print(len(d))

    elif command[0] == "6":
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "7":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])

    elif command[0] == "8":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])