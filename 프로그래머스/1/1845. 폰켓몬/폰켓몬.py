def solution(nums):
    choice = len(nums) // 2 # 선택 수는 nums의 절반
    pokemon = list(set(nums)) # 같은 종류의 포켓몬을 set으로 중복 제거
    return min(len(pokemon), choice)