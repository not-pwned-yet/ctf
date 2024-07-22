encrypted = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"
decrypted = ''.join(chr(ord(c) ^ 5) for c in encrypted)
print(decrypted)

