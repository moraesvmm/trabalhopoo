from modelos.pet import Pet
from modelos.servicos import Servico
import datetime

""" Associa pet, serviço, data, horário e calcula valor """
class Agendamento():
    def __init__(self, pet : Pet, servico : Servico, data : datetime):
        self._pet = pet
        self._servico = servico
        self._data = data.date()
        self._hora = data.time()
        