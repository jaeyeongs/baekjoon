def solution(players, callings):
    player = {j : int(i) for i, j in enumerate(players)}
    for i in callings:
        rank = player[i]
        player[i] -= 1
        player[players[rank-1]] += 1
        players[rank-1], players[rank] = i, players[rank-1]
    return players