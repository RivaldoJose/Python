class Pessoa:
    def __init__(self, nome , idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        if ((not self.falando ) and ( not self.comendo )) :
            self.comendo = True
            print(f"{ self.nome } está comendo")
            return
        else:
            if self.comendo:
                print(f"{self.nome} já está comendo")
                return

            print(f"{self.nome} não pode comer e falar ao mesmo tempo")
            return

    def pararComer(self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} parou de comer")
            return
        else:
            print(f"{self.nome} não tem como parar de comer, já que nem comecei")
            return

    def falar(self):
        if  (not self.comendo) and (not self.falando):
            self.falando = True
            print(f"{self.nome} está falando")
            return
        else:
            if (self.falando == True):
                print(f"{self.nome} já está falando")
                return
            print(f"{self.nome} não pode falar enquanto come")
    
    def pararFalar(self):
        if self.falando:
            self.falando = False
            print(f"{self.nome} parou de falar")
            return
        else:
            print(f"{self.nome} não começou a falar para poder parar de faze-lo XD")
            return