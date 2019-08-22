"""
Binet's Formula For Fibonacci Sequence

"""

PHI = (5 ** (1/2) + 1) / 2

fibonacci = lambda n: int((PHI ** n - (-PHI) ** -n) / (5 ** (1/2)))
