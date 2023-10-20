def solution(nums):
    choice = len(nums) // 2
    pokemon = list(set(nums))
    return min(len(pokemon), choice)