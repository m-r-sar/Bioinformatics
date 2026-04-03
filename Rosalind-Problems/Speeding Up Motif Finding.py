def function(s):
    LPS = [0] * len(s)
    l = 0
    for i in range(1, len(s)):
        if s[i] == s[l]:
            LPS[i] = LPS[i-1] + 1
            l += 1
        else:
            if l != 0:
                l = LPS[l-1]
                if s[i] == s[l]:
                    LPS[i] = l + 1
                    l += 1

    return LPS
