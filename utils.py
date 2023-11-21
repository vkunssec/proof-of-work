import hashlib


NPROCESSES = 4
NTHREADS = 4
PROOF = 4
TARGET = "0" * PROOF


def calculate_hash(data):
    sha = hashlib.sha256()
    sha.update(str(data).encode('utf-8'))
    return sha.hexdigest()
