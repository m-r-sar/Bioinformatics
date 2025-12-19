def Mendels_First_Law(k, m ,n):
    sum = k+m+n
    win_chance = ((k/sum + m/sum * k/(sum-1) + n/sum * k/(sum-1)) +
                  (m/sum * (m-1)/(sum-1) * 3/4 + n/sum * m/(sum-1) * 1/2) +
                  (m/sum * n/(sum-1) * 1/2))
    return win_chance
