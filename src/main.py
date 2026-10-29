from src.modelos.servicos import Banho, Servico, Tosa
""" Importa a classe 'Tutor' do arquivo tutor.py dentro da pasta
/modelos. """

def main() -> None:
    """Mostra os serviços disponíveis no pet shop."""
    servicos: list[Servico] = [Banho(), Tosa()]

    print("========== SERVIÇOS DO PET SHOP ==========")

    for numero, servico in enumerate(servicos, start=1):
        print(f"{numero} - {servico}")
        """Uso do Polimorfismo para percorrer os dois objetos
        em uma mesma lista e cada um exibe seu valor."""


if __name__ == "__main__":
    main()