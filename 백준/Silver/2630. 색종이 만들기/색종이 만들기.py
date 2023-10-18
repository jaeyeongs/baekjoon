n = int(input())
paper = []
result = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

# 재귀, 분할 개념 필요
def cut(x, y, n):
  a = paper[x][y] # 시작점
  for i in range(x, x+n):
    for j in range(y, y+n):
      if a != paper[i][j]:
        cut(x, y, n//2)
        cut(x, y+n//2, n//2)
        cut(x+n//2, y, n//2)
        cut(x+n//2, y+n//2, n//2)
        return

  if a == 0 :
    result.append(0)
  else :
    result.append(1)

cut(0 ,0, n)
print(result.count(0))
print(result.count(1))