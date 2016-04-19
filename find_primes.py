# Exercise 3.33 (Find prime numbers.)
def findPrimes(N):
    '''
    Uses sieve of Eratosthenes to find all primes between 1 and N, inclusive
    '''
    a = [1]*(N+1)
    p = []
    for i in range(2,N+1):
        if a[i] == 0:
            False
        else:
            p.append(i)   
            j = 2*i
            while j <= N:
                a[j] = 0
                j += i
    return p

N = 200
p = findPrimes(N)
print 'Primes less than or equal to', N, 'are...'
print (p)

"""
Primes less than or equal to 200 are...
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
"""
