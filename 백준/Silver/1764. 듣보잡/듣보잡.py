import sys

N, M = map(int, sys.stdin.readline().split())
N_list = set()
M_list = set()

for i in range(N):
    N_list.add(input())

for i in range(M):
    M_list.add(input())

NM_list = sorted(list(N_list & M_list))

print(len(NM_list))
for i in NM_list:
    print(i)