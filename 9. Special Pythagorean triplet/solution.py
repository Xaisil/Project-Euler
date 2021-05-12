import itertools
from math import sqrt
squares = [x**2 for x in range(2,500)]
comb = list(itertools.combinations(squares, 2))
triplets = []
for c in comb:
    if (c[0]+c[1]) in squares and sqrt(c[0])+sqrt(c[1])+sqrt(c[0]+c[1])==1000:
        print(c[0],c[1],c[0]+c[1])
        print(sqrt(c[0])*sqrt(c[1])*sqrt(c[0]+c[1]))