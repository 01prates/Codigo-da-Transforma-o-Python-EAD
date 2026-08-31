class Carro:
    # Método especial de inicialização
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método especial para representação textual
    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    # Personaliza a representação textual para veículos elétricos
    def __str__(self):
        return f"Carro Elétrico: {self.marca} {self.modelo} (Autonomia: {self.autonomia_bateria} km)"


# --- Testando a Atividade 3 ---
if __name__ == "__main__":
    c1 = Carro("Honda", "Civic")
    c2 = CarroEletrico("BYD", "Dolphin", 400)

    # Ao usar print(), o Python chama automaticamente o método __str__
    print(c1)
    print(c2)