def count_unique_substrings(s, n):
    suffixes = sorted([s[i:] for i in range(n)])
    total_substrings = n * (n + 1) // 2

    lcp_sum = 0
    for i in range(1, n):
        s1 = suffixes[i - 1]
        s2 = suffixes[i]

        l = 0
        min_len = min(len(s1), len(s2))
        while l < min_len and s1[l] == s2[l]:
            l += 1
        lcp_sum += l

    return total_substrings - lcp_sum


def function(s):
    a = 4
    n = len(s)
    total_sub = count_unique_substrings(s, n)
    total_max = 0
    for k in range(1, n+1):
        max_substrings = min(a**k, n-k+1)
        total_max += max_substrings

    return round(total_sub / total_max, 4)