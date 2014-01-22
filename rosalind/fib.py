# Problem http://rosalind.info/problems/fib/
# Rabbits and Recurrence Relations

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs.

import sys

def mateRabbits(n, k):
    children = 0
    adult = 1
    for i in range(1, n - 1):
        newborn = adult * k
        adult += children
        children = newborn
    return children + adult

for filename in sys.argv[1:]:
    for line in open(filename):
        numList = line.split()
        n = int(numList[0]) #months
        k = int(numList[1]) #litter
        rabbits = mateRabbits(n, k)
        print(rabbits)        
        
