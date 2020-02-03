import hashlib

#cript = hashlib.md5()
#texto = input('Digite o que quer criptografar: ')
#cript.update(b,"%s"%texto)

#print(cript.hexdigest())

str = "fwk@2019"

result = hashlib.md5(str.encode()) 

print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 