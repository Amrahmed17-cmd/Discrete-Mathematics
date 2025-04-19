from .factorial import fact

def permutations(n, r):
    """Calculate permutations (nPr)"""
    nPr = fact(n) // fact(n - r)
    return nPr 