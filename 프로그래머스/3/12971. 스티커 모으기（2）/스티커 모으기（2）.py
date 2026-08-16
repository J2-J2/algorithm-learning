def find(sticker):
    dp = [0] * len(sticker)
    if len(sticker) == 1: return sticker[0]
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    return dp[-1]


def solution(sticker):
    if len(sticker) == 1: return sticker[0]

    answer = max(find(sticker[:-1]), find(sticker[1:]))

    return answer