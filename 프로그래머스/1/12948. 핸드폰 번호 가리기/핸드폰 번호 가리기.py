def solution(phone_number):
    # length = len(phone_number) - 4
    # answer = phone_number.replace(phone_number[0:length], '*' * length)
    answer = "*" * (len(phone_number)-4) + phone_number[-4:]
    return answer