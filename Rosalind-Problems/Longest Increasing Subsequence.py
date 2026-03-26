import bisect

def function(n, seq):
    def get_lis(seq):
        tails = []  # Stores the smallest tail of increasing subsequences
        tail_indices = []  # Stores the original indices of the elements in 'tails'
        parent = [-1] * len(seq)  # To reconstruct the path of the subsequence

        for i, x in enumerate(seq):
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
                tail_indices.append(i)
            else:
                tails[idx] = x
                tail_indices[idx] = i
            if idx > 0:
                parent[i] = tail_indices[idx - 1]

        if not tail_indices:
            return []

        curr = tail_indices[-1]
        lis = []

        # Trace backwards through the parent array
        while curr != -1:
            lis.append(seq[curr])
            curr = parent[curr]

        return lis[::-1]

    inc_subseq = get_lis(seq)
    negated_seq = [-x for x in seq]
    dec_subseq = [-x for x in get_lis(negated_seq)]

    return inc_subseq, dec_subseq
