def Calculating_Expected_Offspring(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa):
    offspring_AAAA = AAAA*2
    offspring_AAAa = AAAa*2
    offspring_AAaa = AAaa*2
    offspring_AaAa = AaAa*2*3 / 4
    offspring_Aaaa = Aaaa
    offspring_aaaa = 0

    offspring = offspring_AAAA + offspring_AAAa + offspring_AAaa + offspring_AaAa + offspring_Aaaa + offspring_aaaa
    return offspring
