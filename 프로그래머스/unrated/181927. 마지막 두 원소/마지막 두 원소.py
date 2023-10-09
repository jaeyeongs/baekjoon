def solution(num_list):
    if num_list[-1] > num_list[-2]:
        new1 = num_list[-1] - num_list[-2]
        num_list.append(new1)
    else:
        new2 = num_list[-1]*2
        num_list.append(new2)
    return num_list
