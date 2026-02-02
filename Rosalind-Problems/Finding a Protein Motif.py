import requests

#finding the N-glycosylation motif - N{P}[ST]{P}

def Parse_FASTA_uniprot(filename):
    result = {}
    string = []
    with open(filename) as file:
        for line in file:
            string.append(line)
    string = ''.join(string)
    string = string.split(">")
    string.remove(string[0])
    for s in string:
        s = s.split('\n')
        s[0] = s[0].split("|") #
        s[0] = s[0][1] #
        s[1] = "".join(s[1:])
        result.update({s[0]: s[1]})

    return result

def get_FASTA():
    proteins = []
    with open("proteins_to_search.txt") as file:
        for line in file:
            proteins.append(line.strip())

    list = []
    for protein in proteins:
        id = protein
        if not len(protein) == 6:
            id = protein[0:6]
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        r = requests.get(url)
        list.append(r.text)

    with open("proteins.txt", "w", encoding="utf-8") as f:
        for line in list:
            f.write(line)

    return proteins

def finding_motif():
    proteins = Parse_FASTA_uniprot("proteins.txt")
    result = {}
    for protein in proteins:
        positions = []
        sequence = proteins[protein]
        for i in range(len(sequence)):
            motif = sequence[i:i + 4]
            if len(motif) < 4:
                break
            if  motif[0] == "N" and motif[1] != "P" and (motif[2] == "S" or motif[2] == "T") and motif[3] != "P":
                positions.append(str(i + 1))

        positions = " ".join(positions)
        result[protein] = positions
    return result

full_ids = get_FASTA()
result = finding_motif()
i = 0
for protein in result:
    if result[protein]:
        print(full_ids[i])
        print(result[protein])
    i += 1
