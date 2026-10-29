from src.modelos.tutor import Tutor
""" Importa a classe 'Tutor' do arquivo tutor.py dentro da pasta
/modelos. """

def main () -> None:
    """Demonstração de criação e validação dos tutores. """
    tutor = Tutor("Mariana", "(11) 99999-1234")
    print("Tutor cadastrado:")
    print(tutor)

    outro_tutor = Tutor.from_string("Carlos;21988887777")
    print(outro_tutor)

    print(f"\nTotal de tutores criados: {Tutor.total_criados}")

    try:
        tutor.telefone = "123"
    except ValueError as erro:
        print(f"\n Erro esperado: {erro}")

    print(f"Telefone mantido após o erro: {tutor.telefone}")


if __name__ == "__main__":
    main()