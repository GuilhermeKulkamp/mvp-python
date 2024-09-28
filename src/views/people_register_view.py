import os
from typing import Dict

class PeopleRegisterView:
    def registry_person_view(self) -> Dict:
        os.system("cls||clear")


        print("Cadastrar nova pessoa \n\n")

        name = input('Nome da pessoa: ')
        weight = input('Peso da pessoa: ') 
        height = input('Altura da pessoa: ')

        new_person_informations = {
            "name": name, "weight": weight, "height": height
        }

        return new_person_informations