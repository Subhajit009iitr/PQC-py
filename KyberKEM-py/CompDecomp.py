"""
The code for compression and decompression step of polynomials
"""
from utility import round_up

def compress(x,d,q):
    """
    Decompress the polynomial by decompressing each coefficent
    NOTE: This as compression is lossy, we have
    x' = decompress(compress(x)), which x' != x, but is 
    close in magnitude.
    """
    compress_mod = 2**d
    compress_float = compress_mod/q
    return round_up(compress_float*x)

def decompress(x,d,q):
    """
    Decompress the polynomial by decompressing each coefficent
    NOTE: This as compression is lossy, we have
    x' = decompress(compress(x)), which x' != x, but is 
    close in magnitude.
    """
    decompress_float = q/2**d
    return (decompress_float*x)

def encode():

def decode():
