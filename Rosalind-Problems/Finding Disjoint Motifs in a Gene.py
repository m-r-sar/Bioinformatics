def is_interleave(window, p1, p2):
    """
    Checks if 'window' can be formed by interleaving characters of p1 and p2
    while maintaining their relative order.
    """
    l1, l2 = len(p1), len(p2)

    if l1 + l2 != len(window):
        return False

    dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
    dp[0][0] = True

    for i in range(1, l1 + 1):
        dp[i][0] = dp[i - 1][0] and p1[i - 1] == window[i - 1]

    for j in range(1, l2 + 1):
        dp[0][j] = dp[0][j - 1] and p2[j - 1] == window[j - 1]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            dp[i][j] = (dp[i - 1][j] and p1[i - 1] == window[i + j - 1]) or \
                       (dp[i][j - 1] and p2[j - 1] == window[i + j - 1])

    return dp[l1][l2]


def function(s, patterns):
    n = len(patterns)
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        pattern = patterns[i]
        for j in range(n):
            p = patterns[j]

            size = len(pattern) + len(p)
            if size > len(s):
                continue

            for k in range(len(s)):
                window = s[k:k+size]
                if is_interleave(window, p, pattern):
                    M[i][j] = 1
                    break

    return M
