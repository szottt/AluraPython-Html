class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError('Url Invalida!!')

    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        indiceInicialModedaDestino  = self.url.find("=",15) +1

        IndiceInicialModedaOrigem     = self.url.find("=") +1
        indiceFinalModedaOrigem   = self.url.find("&")

        moedaOrigem = self.url[IndiceInicialModedaOrigem:indiceFinalModedaOrigem]
        moedaDestino = self.url[indiceInicialModedaDestino:]

        return moedaOrigem, moedaDestino