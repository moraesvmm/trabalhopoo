class Tutor: 
    """ Representa o responsável por um ou mais pets """

    total_criados = 0

    def __init__(self, nome:str, telefone: str) -> None:
        self.nome = nome
        self.telefone = telefone
        Tutor.total_criados += 1

    @property
    def nome(self) -> str:
        """Retorna o nome do tutor."""
        return self._nome