def solution(A):
    import itertools
    length = len(A) # length of array A

    B = []# lift for ordinal number of A
    for i in range(length - 1):
        B.append(i)

    comb = list(itertools.combinations(B, 2)) # combination numbeer
    comb2 = []
    result = []
    n_comb = len(comb)
    
    for i in range(n_comb - 1):
        c = list(comb[i])
        #print(c) #for test
        cont =A[c[0]] + A[c[1]]
        result.append(cont)
    return min(result)
