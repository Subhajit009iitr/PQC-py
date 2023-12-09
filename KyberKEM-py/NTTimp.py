from sympy import ntt
def BitReversal(i, k):
        """
        bit reversal of an unsigned k-bit integer i
        """
        bin_i = bin(i & (2**k - 1))[2:].zfill(k)
        return int(bin_i[::-1], 2)

