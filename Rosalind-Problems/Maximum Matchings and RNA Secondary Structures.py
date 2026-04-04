import math
def function(s):
    au_count = [s.count('A'), s.count('U')]
    cg_count = [s.count('C'), s.count('G')]

    return math.perm(max(au_count), min(au_count)) * math.perm(max(cg_count), min(cg_count))
