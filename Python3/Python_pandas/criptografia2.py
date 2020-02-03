from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Fwk@2019")
plain_text = cipher_suite.decrypt(cipher_text)

print(f'A senha Encriptada foi {cipher_text}')
print(f'E a senha normal é {plain_text}')