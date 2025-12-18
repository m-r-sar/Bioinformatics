def Rabbits_and_Recurrence_Relations(n, k):
    count_n1 = 1
    count_n2 = 1
    for i in range(n-2):
        count_n = (count_n1 + count_n2 * k)
        count_n2 = count_n1
        count_n1 = count_n
    return count_n
