def solution(k, m, score):
    answer = 0
    # 사과 점수를 내림차순으로 나열
    # [1, 2, 3, 1, 2, 3, 1] -> [3,3,2,2,1,1,1]
    score = sorted(score, reverse=True)
    
    # 사과의 개수(len(score)) 횟수를 m개씩 순회
    for i in range(0, len(score), m):
        box = score[i:i+m] # 박스에 사과 점수를 4개씩 저장
        
        # 상자 안에 4개가 담기면
        if len(box) == m:
            answer += min(box)*m # 담긴 박스의 최저 점수 * 사과 개수
    
    return answer