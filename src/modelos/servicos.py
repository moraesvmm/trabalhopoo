from abc import ABC, abstractmethod

class Servico(ABC):
    """Define o que todos os serviços do pet shop devem ter."""

    def __init__(self, nome:str) -> None:
        self.nome = nome


    @abstractmethod
    def calcular_preco(self) -> float:
        """Retorna o preço do serviço."""
        pass

    def __str__(self) -> str:
        """Retorna o nome e o preço do serviço."""
        return f"{self.nome} - R$ {self.calcular_preco():.2f}"


class Banho(Servico):
    """Representa o serviço de banho."""

    PRECO = 40.0

    def __init__(self) -> None:
        super().__init__("Banho")

    def calcular_preco(self) -> float:
        """Retorna o preço do banho."""
        return self.PRECO

class Tosa(Servico):
    """Retorna o serviço de tosa."""

    PRECO = 50.0

    def __init__(self) -> None:
        super().__init__("Tosa")

    def calcular_preco(self) -> float:
        """Retorna o preço da tosa."""
        return self.PRECO

        

