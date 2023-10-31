N = int(input())
result = set()

for i in range(N):
    A, B = input().split()

    if A == "ChongChong" or B == "ChongChong":
        result.add(A)
        result.add(B)

    if A in result or B in result:
        result.add(A)
        result.add(B)
        
print(len(result))