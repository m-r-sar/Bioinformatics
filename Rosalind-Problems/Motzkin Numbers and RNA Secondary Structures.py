def function(s):
    valid_pairs = {"AU", "UA", "GC", "CG"}
    memo = {}

    def count_matchings(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i >= j:
            return 1

        total_matchings = count_matchings(i+1, j)

        for k in range(i + 1, j + 1):
            if s[i] + s[k] in valid_pairs:
                left = count_matchings(i + 1, k - 1)
                right = count_matchings(k + 1, j)

                total_matchings = (total_matchings + (left * right)) % 1000000

        memo[(i, j)] = total_matchings
        return total_matchings

    return count_matchings(0, len(s) - 1)
