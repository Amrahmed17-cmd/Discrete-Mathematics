from .factorial import fact

def combinations(n, r):
    """Calculate combinations (nCr)"""
    nCr = fact(n) // (fact(r) * fact(n - r))
    return nCr 