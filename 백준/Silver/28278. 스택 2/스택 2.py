import sys
input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
    command = input().split()

    if command[0] == "1":
        stack.append(int(command[1]))

    elif command[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == "3":
        print(len(stack))

    elif command[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "5":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])