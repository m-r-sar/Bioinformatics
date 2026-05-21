def function(dataset):
    encoded_columns = []

    for i in range(len(dataset[0])):
        column = ""
        for data in dataset:
            column += data[i]

        unique_bases = list(set(column))

        if len(unique_bases) == 2:
            base1 = unique_bases[0]
            base2 = unique_bases[1]

            if column.count(base1) >= 2 and column.count(base2) >= 2:
                encoded = column.replace(base1, "0").replace(base2, "1")
                encoded_columns.append(encoded)

    return encoded_columns