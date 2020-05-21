from ExtratorArgumentosUrl import ExtratorArgumentosUrl

'''
argumento = 'https://www.bytebank.com.br/cambio?moedaorigem=real'
# index = argumento.find('=')
# subString = argumento[index + 1:]
# print(subString)

# argumento = 'moedaorigem=real'
# print(index)

argumento = 'https://www.bytebank.com.br/cambio?moedaorigem=real'
listaargumento = argumento.split('=')
print(listaargumento)'''

#https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700

url = 'moedaorigem=real&moedadestino=dolar'

argumentosUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaDestino, moedaOrigem)


ExtratorArgumentosUrl.urlEhValida("a")