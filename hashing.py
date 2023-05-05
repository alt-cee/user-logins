import hashlib

if __name__ == "__main__":
    b = bytearray('steveslist', 'utf-8')
    print(hashlib.sha256(b).hexdigest())
    print(hashlib.sha256(b).hexdigest())
    print(hashlib.md5(b).hexdigest())

