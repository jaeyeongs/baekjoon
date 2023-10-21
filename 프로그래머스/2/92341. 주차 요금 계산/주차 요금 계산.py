import math

def parking_minute(date):
    h, m = map(int, date.split(':'))
    minute = h*60 + m
    return minute

def solution(fees, records):
    answer = []
    dic = {}

    for r in records:
        time, number, in_out = r.split() # time:16:00, number:3961, in_out:IN/OUT

        if number in dic:
            dic[number].append([parking_minute(time), in_out])
        else:
            dic[number] = [[parking_minute(time), in_out]]

    rlist = list(dic.items())
    rlist.sort() # print(rlist[0]) -> ('0202', [[960, 'IN'], [1080, 'OUT']])

    for r in rlist:
        t = 0

        for rr in r[1]:
            if rr[1] == 'IN':
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == 'IN':
            t += parking_minute('23:59')

        if t <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((t-fees[0]) / fees[2]) * fees[3])

    return answer