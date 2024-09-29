import os
from typing import Dict

class PeopleRegisterView:
    # página inicial 
    def registry_person_view(self) -> Dict:
        os.system("cls||clear")


        print("Cadastrar nova pessoa \n\n")

        name = input('Informe o Nome: ')
        weight = input('Informe o Peso (em gramas): ') 
        height = input('Informe a Altura (em centímetros): ')

        new_person_informations = {
            "name": name, "weight": weight, "height": height
        }

        return new_person_informations
    
    # página de sucesso
    def registry_person_success(self, message: Dict) -> None:
        os.system("cls||clear")

        success_message = f'''
            Usuário cadastrado com sucesso!

            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
                Nome: {message["attributes"]["name"]}
                Altura: {message["attributes"]["height"]}
                Peso: {message["attributes"]["weight"]}

            '''
        
        print(success_message)
    
    #página da falha
    def registry_person_fail(self, error: str) -> None:
        os.system("cls||clear")

        error_message = f'''
            Falha ao cadastrar o usuário!

            Erro: {error} 
        '''

        print(error_message)
