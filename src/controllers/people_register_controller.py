from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:

        # se tudo der certo retorna o sucesso
        try:
            # validar campos
            self.__validation_field(new_person_informations)

            # enviar para models para cadastro de dados
            # TODO: criar models

            # formatar a resposta
            response = self.__format_response(new_person_informations)

            # retorna sucesso
            return {"success": True, "message": response}
        
        # se houver erro retorna o erro
        except Exception as exception: 
            return {"success": False, "error": str(exception)}
    
    # Regras de validação
    def __validation_field(self, new_person_informations: Dict) -> None:
        # verifica se o nome é uma string
#        try: str(new_person_informations["name"])
#        except: raise Exception("Campo nome incorreto")
        if isinstance(new_person_informations["name"], str):
            raise Exception("Campo nome incorreto!")
        
        # verifica se campo peso é um número inteiro (em gramas)
        try: int(new_person_informations["weight"])
        except: raise Exception("Campo peso incorreto")

        # verifica se campo altura é um número inteiro (em centímetros)
        try: int(new_person_informations["height"])
        except: raise Exception("Campo altura incorreto")

    # Formata a resposta para a view
    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "attributes": new_person_informations
        }
