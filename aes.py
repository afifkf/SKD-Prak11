from Crypto.Cipher import AES

key = b'Yansurmon'

cipher = AES.new(key, AES.MODE_EAX)

data = "Hidup SKD Jaya".encode()

nonce = cipher.nonce

ciphertext = cipher.encrypt(data)

print("Cipher text:", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)