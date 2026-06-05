def function(dataset):
    max_length = len(max(dataset, key=len))
    total_length = sum(len(contig) for contig in dataset)
    N50 = 0
    N75 = 0
    for i in range(max_length, 1, -1):
        i_length = sum(len(contig) for contig in dataset if len(contig) >= i)
        if i_length >= total_length*0.75 and N75 == 0:
            N75 = i
        if i_length >= total_length*0.5 and N50 == 0:
            N50 = i
    return N50, N75
