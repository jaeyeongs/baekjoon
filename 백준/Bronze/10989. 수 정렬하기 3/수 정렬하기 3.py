import sys

N = int(sys.stdin.readline())
num = [0] * 10001 # 10,000보다 작거나 같은 자연수이기 때문에 미리 리스트에 0 할당

for _ in range(N):
    num[int(sys.stdin.readline())] += 1 # for문에서 append 사용하면 메모리 재할당 때문에 메모리 초과

for i in range(10001):
    if num[i] != 0: # 0이 아닌 값의 인덱스
        for j in range(num[i]): # 0이 아닌 값의 개수만큼 반복
            print(i) # 해당하는 인덱스 출력