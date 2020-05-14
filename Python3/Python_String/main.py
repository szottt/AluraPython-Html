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

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real'
print(ExtratorArgumentosUrl.urlEhValida(url))