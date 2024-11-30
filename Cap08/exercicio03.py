class Smartphone():
    def __init__(self, tamanho = '15.99', interface = '6.5'):
        self.tamanho = tamanho
        self.interface = interface

    def imprimir(self):
        print('Dimencoes Smartphone')
        print('Tamanho: ' + self.tamanho)
        print('Interface: ' + self.interface)

smart = Smartphone()
smart.imprimir()

class mp3Player(Smartphone):
    def __init__(self):
        Smartphone.__init__(self)
    def imprimir(self):
        print('Dimencoes mp3Player')
        print('Tamanho: ' + self.tamanho)
        print('Interface: ' + self.interface)

mp3 = mp3Player()
mp3.imprimir()