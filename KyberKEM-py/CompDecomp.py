"""
The code for compression and decompression step of polynomials
"""
from utility import round_up, bitstring_to_bytes, bytes_to_bits

def compress(x,d,q):
    """
    Compress the polynomial by compressing each coefficent
    NOTE: This is lossy compression
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

# print(compress(6,3,16))
# print(decompress(3,3,16))

def encode(coef, l=None):
    if l is None:
        l = max(x.bit_length() for x in coef)
    bit_string = ''.join(format(c,f'0{1}b')[::-1] for c in coef)
    return bitstring_to_bytes(bit_string)


def decode(n, input_bytes, l=None, is_ntt=False):
    if l is None:
            l, check = divmod(8*len(input_bytes), n)
            if check != 0:
                raise ValueError("input bytes must be a multiple of (polynomial degree) / 8")
    else:
        if n*l != len(input_bytes)*8:
            raise ValueError("input bytes must be a multiple of (polynomial degree) / 8")
    coefficients = [0 for _ in range(n)]
    list_of_bits = bytes_to_bits(input_bytes)
    for i in range(n):
        coefficients[i] = sum(list_of_bits[i*l + j] << j for j in range(l))
    return coefficients, is_ntt
