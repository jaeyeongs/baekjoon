def solution(brown, yellow):
    answer = []
    for i in range(3,((brown-2)//2)+1):
        brown_width = (brown - ((i - 2) * 2)) // 2
        yellow_width = brown_width - 2
        yellow_height = i - 2
        
        width = brown_width
        height = i
        if yellow == yellow_width * yellow_height:
            if width >= height:
                answer = [width, height]

    return answer