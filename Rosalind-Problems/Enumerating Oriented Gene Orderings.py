import math
def function(a):
    results = []
    total = math.factorial(a) * (2 ** a)

    def build_permutation(current_permutation):
        if len(current_permutation) == a:
            results.append(current_permutation.copy())
            return
        else:
            used_bases = set()
            for i in range(1, a+1):
                if i not in used_bases:
                    used_bases.add(i)
                    current_permutation.append(i)
                    build_permutation(current_permutation)
                    current_permutation.pop()
                    used_bases.remove(i)

                    used_bases.add(i)
                    current_permutation.append(-i)
                    build_permutation(current_permutation)
                    current_permutation.pop()
                    used_bases.remove(i)

    build_permutation([])
    return total, results
