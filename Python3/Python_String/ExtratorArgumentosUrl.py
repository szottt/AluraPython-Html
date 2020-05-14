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
