def solution(info, n, m):
    a_total = sum(a for a, b in info)
    b_total = sum(b for a, b in info)

    if b_total < m:
        return 0

    cap = m - 1  # B가 버틸 수 있는 최대 흔적
    if cap < 0:
        return -1

    dp = [-1] * (cap + 1)
    dp[0] = 0
    for a, b in info:
        for j in range(cap, b - 1, -1):
            if dp[j - b] != -1:
                dp[j] = max(dp[j], dp[j - b] + a)

    best_b_side_a = max(v for v in dp if v != -1)  # dp[0]=0 always exists
    a_remain = a_total - best_b_side_a
    return a_remain if a_remain < n else -1