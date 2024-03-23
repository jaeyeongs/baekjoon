def solution(s):
    answer = []
    words = s.split(" ")
    
    for word in words:
        new_word = ''
        
        for idx, alp in enumerate(word):
            if idx % 2 == 0:
                new_word += alp.upper()
            else:
                new_word += alp.lower()
                
        answer.append(new_word)

    return " ".join(answer)