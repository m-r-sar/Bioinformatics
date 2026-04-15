def function(n, s1, s2):
    union = s1.union(s2)
    intersection = s1.intersection(s2)
    difference_s1 = s1.difference(s2)
    difference_s2 = s2.difference(s1)
    complement_s1 = (set(i for i in range(1, n+1))).difference(s1)
    complement_s2 = (set(i for i in range(1, n+1))).difference(s2)

    return union, intersection, difference_s1, difference_s2, complement_s1, complement_s2
