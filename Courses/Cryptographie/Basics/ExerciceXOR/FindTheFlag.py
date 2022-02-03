def brute(input, key):
    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    return output.decode("utf-8")

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = bytes.fromhex(data)
print("[-] CIPHER: {}".format(cipher))

# First Step
key_part = brute(cipher[:7], "crypto{".encode())
print("[-] PARTIAL KEY FOUND: {}".format(key_part))

# Second Step
key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key))/len(key))
key += key[:((len(cipher) - len(key))%len(key))]
print("[-] Decoding using KEY: {}".format(key))

plain = brute(cipher, key)
print("\n[*] FLAG: {}".format(plain))