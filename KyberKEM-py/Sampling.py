from climax import q,n
from utility import bytes_to_bits
def parse(b):
    """
    Rq . Kyber uses a deterministic approach to sample elements in Rq that are
    statistically close to a uniformly random distribution. For this sampling we use a function Parse : B* → Rq ,
    which receives as input a byte stream B = b0 , b1 , b2 , . . . and computes the NTT-representation â = â0 +
    â1 X + · · · + ân-1 X n-1 ∈ Rq of a ∈ Rq .
    """
    i = 0
    j = 0
    a = [0]*n
    while(j<n):
        d1 = b[i] + 256*(b[i+1]%256)
        d2 = b[i+1]/16 + 16*b[i+2]
        if(d1<q):
            a[j] = d1
            j = j + 1
        if((d2<q) and (j<n)):
            a[j] = d2
            j = j + 1
        i = i + 3
    return a

def CBD(b,eta):
    """
    Algorithm 2 (Centered Binomial Distribution)
    https://pq-crystals.org/kyber/data/kyber-specification-round3-20210804.pdf
        
    Expects a byte array of length (eta * deg / 4)
    For Kyber, this is 64 eta.
    """
    beta = bytes_to_bits(b)
    f = [0]*n
   
    for i in range(n):
        a = sum(beta[2*i*eta + j]for j in range(eta))
        c = sum(beta[2*i*eta + eta + j]for j in range(eta))
        f[i] = a - c
    return f







