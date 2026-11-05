from __future__ import annotations
from abc import ABC, abstractmethod
from modelos.tutor import Tutor

PORTE : dict[int, str] = {
    1 : "PEQUENO",
    2 : "MEDIO",
    3 : "GRANDE"
}

class Pet(ABC):
    """ Guarda o nome, espécie, porte e tutor que pertence"""
    def __init__(self, animal : str, nome : str, especie : str, porte : str, tutor : Tutor, peso : float) -> None:
        self._animal = animal
        self._nome =  nome.upper()
        self._especie = especie.upper()
        self._validar_porte(porte)
        self._tutor_reponsavel = tutor
        self._peso = peso
    
    @property
    def animal(self) -> str:
        return self._animal
    
    @property
    def porte(self) -> str:
        return self._porte
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def especie(self) -> str:
        return self._especie
    
    @property
    def tutor(self) -> Tutor:
        return self._tutor_reponsavel
    
    @porte.setter
    def porte(self, porte : str):
        self._validar_porte(porte)
    
    def _validar_porte(self, porte : str) -> None :
        porte_validado = porte.upper()
        if porte_validado not in PORTE.values():
            raise ValueError(f"Porte inválido. Use um destes: {PORTE.values()}")
        self._porte = porte_validado
    
    @staticmethod
    def procurar_pet(nome_pet : str) -> str :
        """ Procura o pet a partir do nome na lista. """
        for pet in pets:
            if pet._nome == nome_pet.upper():
                return pet
        print("Não encontrado.")
    
    @staticmethod
    def cadastrar_pet(pet_cadastrar : Pet) -> None:
        """ Cadastra um pet (seja que animal for) em uma lista """
        novo_pet : Pet = pet_cadastrar
        pets.append(novo_pet)
    
    def __str__(self) -> str:
        """ Retorna o descritivo do pet junto do animal que é """
        return f"{self.animal.upper()} com o nome {self.nome} - {self.especie} sob cuidados do {self.tutor}"

class Cachorro(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__("Cachorro", nome, especie, porte, tutor, peso)
        
class Gato(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__("Gato", nome, especie, porte, tutor, peso)

class Cavalo(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__("Cavalo", nome, especie, porte, tutor, peso)

class Lontra(Pet):
    def __init__(self, nome, especie, porte, tutor, peso) -> None:
        super().__init__("Lontra", nome, especie, porte, tutor, peso)
        
pets : list[Pet] = []