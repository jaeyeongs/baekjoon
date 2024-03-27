def solution(n, control):
    alp_dic = {'w' : 1,
              's' : -1,
              'd' : 10,
              'a' : -10}
    
    for i in control:
        n += alp_dic[i]
            
    return n