def solution(array, commands):
    answer = []
    
    # i, j, k에 2차원 배열의 원소 담기
    for i, j, k in commands:
        a = sorted(array[i-1:j]) # i-1:j 까지 슬라이싱하고 오름차순 나열
        answer.append(a[k-1]) # k-1번째 원소 추가
        
    return answer