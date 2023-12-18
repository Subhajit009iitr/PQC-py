import numpy as np

from climax import q, n

from reduction import barrett_reduce, fqmul, mont, r, rr, r_inv,montgomery_reduce

n_inv = pow(n, -1, q) * r % q

def reverse_bits(n):
    b = "{:0{width}b}".format(n, width=7)
    return int(b[::-1], 2)

positions = [reverse_bits(x) for x in range(0, n)]

psi = 1

root = 17

tmp = []

psis = []

inv_psis = []

for x in range(0, n):
    tmp.append(psi)
    psi = psi * root % q

for x in range(0, n):
    val = tmp[positions[x]]
    inv_val = pow(val, -1, q)
    psis.append(val * r % q)
    inv_psis.append(inv_val * r % q)


# Cooley-Tukey (TC) no(natural order) -> br (bit reversed order)

def ntt(a):
    t = n
    m = 1
    while m < n:
        t = t // 2
        for i in range(0, m):
            j1 = 2 * i * t
            j2 = j1 + t - 1
            S = psis[m + i]
            for j in range(j1, j2 + 1):
                U = a[j]
                V = fqmul(a[j + t], S)
                a[j] = barrett_reduce(U + V)
                a[j + t] = barrett_reduce(U - V)
        m = 2 * m

# Gentleman-Sande (GS)  br (bit reversed order) -> no (natural order)

def inv_ntt(a):
    t = 1
    m = n
    while m > 1:
        j1 = 0
        h = m // 2
        for i in range(0, h):
            j2 = j1 + t - 1
            S = inv_psis[h + i]
            for j in range(j1, j2 + 1):
                U = a[j]
                V = a[j + t]
                a[j] = barrett_reduce(U + V)
                a[j + t] = fqmul(S, U - V)
            j1 = j1 + 2 * t
        t = 2 * t
        m = m // 2
    for i in range(0, n):
        a[i] = fqmul(a[i], n_inv)


f = np.zeros(n + 1)
f[0] = 1
f[n] = 1

a = np.random.randint(0, q, n)

b = np.random.randint(0, q, n)

p = np.remainder(np.polydiv(np.polymul(a[::-1], b[::-1]), f)[1], q).astype(int)[::-1]

print(p)

a = np.array([montgomery_reduce(x * rr) for x in a])

b = np.array([montgomery_reduce(x * rr) for x in b])

ntt(a)
ntt(b)
c = np.array([fqmul(x, y) for (x, y) in zip(a, b)])

inv_ntt(c)

c = np.array([montgomery_reduce(x) for x in c])

print(c)

print(np.array_equal(c, p))