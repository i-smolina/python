# Problem http://rosalind.info/problems/iprb/
# Mendel's First Law

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate.

import sys

# get binomial coefficient C(n, k)
# Pascal's triangle
def binom(n, k):
    binomc = [[1]]
    for i in range(1, n + 1):
        row = [1]
        for j in range(1, i):
            if j > k: # cut triangle by number k
                break
            row.append(binomc[i - 1][j - 1] + binomc[i - 1][j])
        if len(row) <= k:
            row.append(1)
        binomc.append(row)            
    return binomc[n][k]

for filename in sys.argv[1:]:
    for line in open(filename):
        numList = line.split()
        k = int(numList[0]) # homozygous dominant (AA)
        m = int(numList[1]) # heterozygous (Aa)
        n = int(numList[2]) # homozygous recessive (aa)
        print(binom(4,2))
        # AA + AA
        i1 = binom(k, 2) * 4
        # AA + Aa
        i2 = k * m * 4
        # AA + aa
        i3 = k * n * 4
        # Aa + Aa
        i4 = binom(m, 2) * 3
        # Aa + aa
        i5 = m * n * 2
        # count variants of all alleles in the population
        N = binom(k + m + n, 2) * 4
        P = (i1 + i2 + i3 + i4 + i5) / N # the probability of a offspring's dominant allele
        print(P)
       
        
