def solution(M, F):
    M, F = long(M), long(F)
    total = 0
    while not (M == 1 and F == 1):
        if F <= 0 or M <= 0:
            return "impossible"
        if F == 1:
            return str(total + M - 1)
        else:
            total += long(M/F)
            M, F = F, M % F
    return str(total)
