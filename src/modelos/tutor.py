class Tutor:
    """Representa o responsável por um pet."""
    total_criados : int = 0
    def __init__(self, nome:str, telefone:str) -> None:
        self._nome = nome
        if self.validar_telefone(telefone):
            self._telefone = telefone
        self.total_criados += 1 
    
    @property 
    def nome(self) -> str:
        """Retorna o nome do tutor."""
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        """Valida e armazena o nome do tutor."""
        nome = valor.strip()

        if not nome:
            raise ValueError("O nome não pode ficar vazio.")

        self._nome = nome

    @property
    def telefone(self) -> str:
        """Retorna o telefone do tutor."""
        return self._telefone

    @telefone.setter
    def telefone(self, valor: str) -> None:
        """Valida e armazena o telefone do tutor."""
        if not self.validar_telefone(valor):
            raise ValueError("O telefone deve ter 10 ou 11 dígitos")

        self._telefone = "".join(
            caractere for caractere in valor if caractere.isdigit()
        )

    def validar_telefone(telefone: str) -> bool:
        """Verifica se o telefone tem 10 ou 11 dígitos."""
        if not isinstance(telefone, str):
            return False
            
        digitos = "".join(
            caractere for caractere in telefone if caractere.isdigit()
        )
        return len(digitos) in (10, 11)
    
    @staticmethod
    def cadastrar_tutor() -> "Tutor":
        """ Método que cria um objeto Tutor. """
        nome_tutor : str = input("Insira o nome do tutor: ")
        telefone_tutor : str = input("Insira o telefone do tutor\nExemplo - XXXXXXXXXXX : ")
        tutor_cadastrar : Tutor = Tutor(nome_tutor, telefone_tutor)
        _tutores.append(tutor_cadastrar)
        print("Tutor cadastrado com sucesso. ")
        return tutor_cadastrar
        
    @classmethod
    def from_string(cls, dados: str) -> "Tutor":
        """Cria um tutor a partir do texto 'nome;telefone'."""
        partes = dados.split(";")

        if len(partes) != 2:
            raise ValueError("Use o formato nome;telefone.")

        nome, telefone = partes
        return cls(nome, telefone)

    def __str__(self) -> str:
        """Retorna uma descrição do tutor."""
        return f"Tutor: {self.nome} - Telefone: {self.telefone}"

_tutores : list[Tutor] = []