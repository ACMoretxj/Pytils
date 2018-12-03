from hashlib import sha256


def sha(content):
    content = str(content).encode()
    return sha256(content).hexdigest()
