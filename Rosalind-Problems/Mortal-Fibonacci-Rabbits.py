def Mortal_Fibonacci_Rabbits(years,max_age):
    rabbits = [0 for _ in range(max_age)]
    rabbits[1] = 1
    for i in range(1,years-1):
        new_rabbits = sum(rabbits[1:])
        for j in range(len(rabbits)):
            try:
                if max_age-j < 0 or max_age-j-1 < 0:
                    pass
                else:
                    rabbits[max_age-j] = rabbits[max_age-j-1]
            except IndexError:
                pass
        rabbits[0] = new_rabbits
    return sum(rabbits)
