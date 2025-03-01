class Poo:
    nome = ""
    fome = 5
    felicidade = 5

    def __init__(self, name):
        self.nome = name
        self.fome = 5
        self.felicidade = 5

    def alimentar(self):
        self.fome -= 1
        if self.fome < 0:
            self.fome = 0

    def brincar(self):
        self.felicidade += 1
        if self.felicidade > 10:
            self.felicidade = 10

    def mostrar_status(self):
        print(f"Nome {self.nome}")
        print(f"Fome {self.fome}, Felicidade {self.felicidade}")


