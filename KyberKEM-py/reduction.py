from climax import q, n

e = 16

r = 1 << e

rr = r * r %q

mont = r % q

r_inv = pow(r, -1, q)

k = (r * r_inv - 1) // q

kbr = 26

m = 2**kbr // q

def barrett_reduce(x):
    x1 = x * m >> kbr
    x -= x1 * q
    if x > q:
        return x - q
    else:
        return x

def montgomery_reduce(x):
    s = x * k & (r - 1)
    t = x + s * q
    u = t >> e
    return u if u < q else u - q

def fqmul(a, b):
    return montgomery_reduce(a * b)