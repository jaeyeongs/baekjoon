# def solution(s):
#     answer = []
#     word = []
    
#     for i in range(len(s)):
#         if s[i] not in word:
#             word.append(s[i])
#             answer.append(-1)
#         else:
#             word.append(s[i])
#             answer.append(i - (s.index(s[i])))
        
#     return answer

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer