def solution(n):
    a = 0
    b = 1
    
    for _ in range(2, n+1):
        b , a = b + a, b
        
    return b % 1234567