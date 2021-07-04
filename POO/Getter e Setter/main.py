
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, desconto):
        self.preco = self.preco - (self.preco * (desconto / 100))

    # GETTER NOME
    @property
    def nome(self):
        return self._nome

    # SETTER NOME
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # GETTER PREÇO
    @property
    def preco(self):
        return self._preco

    # SETTER PREÇO
    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, str):
            novo_preco = float(novo_preco.replace('R$', ''))
        else:
            self._preco = novo_preco

p1 = Produto('Camisa', 50)
p1.desconto(10)
p1.nome = 'Camiseta'
print(p1.nome, " R$", p1.preco)