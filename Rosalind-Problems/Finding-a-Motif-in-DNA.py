def Finding_a_Motif_in_DNA(s, t):
    positions = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            positions.append(str(i+1))

    positions = " ".join(positions)
    return positions
