import hmac
import hashlib
import sys
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

key = b'cookie'
data = b'cake'

def PRF(key, data):
    prf_output = hmac.new(key, data, hashlib.sha256).digest()
    print(prf_output)
    print(sys.getsizeof(prf_output))

def XOF(data):
    xof_output = hashlib.sha3_256(data).digest()
    print(xof_output)
    print(sys.getsizeof(xof_output))

def KDF(key):
    kdf = HKDF(
    algorithm=hashes.SHA256(),
    length=32,  # Output key length in bytes
    salt=None,  # Optional salt
    info=b'additional_info',  # Optional context-specific info
    backend=default_backend()
    )
    derived_key = kdf.derive(key)
    print(derived_key)

KDF(key)