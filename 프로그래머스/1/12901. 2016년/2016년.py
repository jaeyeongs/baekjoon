def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    return day[(sum(month[:a-1]) + b) % 7]

solution(5, 24)