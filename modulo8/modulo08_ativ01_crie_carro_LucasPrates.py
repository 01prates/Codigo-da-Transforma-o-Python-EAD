class Carro:
    def __init__(self, marca: str, modelo: str):
        # O método __init__ inicializa os atributos do objeto
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")

    def __str__(self):
        # O método __str__ personaliza a representação textual do objeto
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        # super() chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria  # Atributo exclusivo

    def exibir_info(self):
        # Sobrescrevemos o método para incluir a autonomia
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Autonomia: {self.autonomia_bateria} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.autonomia_bateria}km de autonomia)"


# Exemplo de uso:
meu_carro = Carro("Toyota", "Corolla")
meu_eletrico = CarroEletrico("Tesla", "Model 3", 500)

meu_carro.exibir_info()
meu_eletrico.exibir_info()