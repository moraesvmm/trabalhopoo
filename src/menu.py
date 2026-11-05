from datetime import datetime
from modelos.servicos import Servico, Banho, Tosa, Hospedagem
from modelos.agendamento import Agendamento
from modelos.pet import Pet, Cachorro, Cavalo, Gato, Lontra
from modelos.tutor import Tutor

agendamentos: list[Agendamento] = []

""" Método para criar interface no cmd.  """
def menu_index() -> None :
    escolha_menu : str = f"""
    {'=' * 10} SISTEMA PET SHOP {'=' * 10}
    1 - Cadastrar Pet
    2 - Cadastrar Tutor
    3 - Listar Serviços
    4 - Buscar Pet
    5 - Novo Agendamento
    6 - Finalizar Pedido
    7 - Relatório Faturamento
    0 - Sair
    """
    menu : int = None
    while menu != 0:
        print(escolha_menu)
        menu = float(input("Digite o que deseja fazer: "))
        match menu:
            case 1 :
                nome_pet : str = input("Digite o nome do pet: ").upper()
                espec_pet : str = input("Digite a especie do pet: ").upper()
                porte_pet : str = input("Pequeno, médio ou grande: ").upper()
                peso_pet : float = input("Peso do Pet: ")
                tutor_pet = Tutor.cadastrar_tutor()
                animal : int = int(input("Qual é o animal: 1 - Cachorro | 2 - Gato | 3 - Cavalo | 4 - Lontra .: "))
                pet_cadastrar : Pet = None
                match animal :
                    case 1 :
                        pet_cadastrar = Cachorro(nome_pet, espec_pet, porte_pet, tutor_pet, peso_pet)
                        Pet.cadastrar_pet(pet_cadastrar)
                        continue
                    case 2 :
                        pet_cadastrar = Gato(nome_pet, espec_pet, porte_pet, tutor_pet, peso_pet)
                        Pet.cadastrar_pet(pet_cadastrar)
                        continue
                    case 3 :
                        pet_cadastrar = Cavalo(nome_pet, espec_pet, porte_pet, tutor_pet, peso_pet)
                        Pet.cadastrar_pet(pet_cadastrar)
                        continue
                    case 4:
                        pet_cadastrar = Lontra(nome_pet, espec_pet, porte_pet, tutor_pet, peso_pet)
                        Pet.cadastrar_pet(pet_cadastrar)
                        continue
                    case _:
                        print("Não existe tipo de animal com esse número. Favor reinsira o número correto!")
                        continue
                input("Pressione enter para continuar...")
                continue
            case 2 :
                Tutor.cadastrar_tutor()
                input("Pressione enter para continuar...")
                continue
            case 3:
                # Mostra os serviços disponíveis no pet shop com seus respectivos preços.
                Servico.listar_servicos()
                input("Pressione enter para continuar...")
                continue
            case 4:
                print(Pet.procurar_pet(input("Insira o nome do pet: ")))
                input("Pressione enter para continuar...")
                continue
            case 5:
                pet_escolhido = Pet.procurar_pet(input("Nome do pet: ").strip())
                if pet_escolhido is None:
                    continue

                print("1 - Banho | 2 - Tosa | 3 - Hospedagem")
                servicos = {1: Banho(), 2: Tosa(), 3: Hospedagem()}
                try:
                    servico_escolhido = servicos[int(input("Escolha o serviço: "))]
                except (ValueError, KeyError):
                    print("Opção de serviço inválida.")
                    continue

                texto_data = input("Data e hora (dd/mm/aaaa hh:mm): ")
                try:
                    data_hora = datetime.strptime(texto_data, "%d/%m/%Y %H:%M")
                except ValueError:
                    print("Data inválida. Use o formato dd/mm/aaaa hh:mm.")
                    continue

                agendamento = Agendamento(pet_escolhido, servico_escolhido, data_hora)
                agendamentos.append(agendamento)
                print("Agendamento realizado com sucesso!")
                continue
            case 6:
                pass
            case 7:
                pass
            case 0:
                exit
            case _:
                print("Favor, inserir um dos números correspondentes!")
                continue
