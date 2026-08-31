class Carro:
    """Classe base para veículos."""

    def __init__(self, marca: str, modelo: str) -> None:
        self._marca = marca
        self._modelo = modelo

    def exibir_info(self) -> None:
        print(f"Marca: {self._marca} | Modelo: {self._modelo}")


class CarroEletrico(Carro):
    """Subclasse que representa um veículo elétrico, estendendo a classe Carro."""

    def __init__(self, marca: str, modelo: str, autonomia_bateria: int) -> None:
        """
        Inicializa um Carro Elétrico.

        :param marca: Fabricante do carro.
        :param modelo: Modelo do carro.
        :param autonomia_bateria: Autonomia em quilômetros (km). Deve ser maior que zero.
        """
        # Chama o construtor da classe pai (Carro)
        super().__init__(marca, modelo)

        if not isinstance(autonomia_bateria, (int, float)) or autonomia_bateria <= 0:
            raise ValueError("A autonomia da bateria deve ser um número maior que zero.")

        self._autonomia_bateria = int(autonomia_bateria)

    @property
    def autonomia_bateria(self) -> int:
        """Retorna a autonomia da bateria em km."""
        return self._autonomia_bateria

    def exibir_info(self) -> None:
        """Exibe as informações do carro elétrico incluindo sua autonomia."""
        print(f"=== VEÍCULO ELÉTRICO ===")
        print(f"Marca     : {self._marca}")
        print(f"Modelo    : {self._modelo}")
        print(f"Autonomia : {self._autonomia_bateria} km")
        print("=" * 26)


# --- Execução da Atividade 2 ---
if __name__ == "__main__":
    eletrico1 = CarroEletrico(marca="Tesla", modelo="Model S", autonomia_bateria=650)
    eletrico1.exibir_info()

    eletrico2 = CarroEletrico(marca="BYD", modelo="Seal", autonomia_bateria=520)
    eletrico2.exibir_info()