from typing import Dict, List
from flask import request as FlaskRequest

'''
* N números são enviados
* Todos esses N números são multiplicados por 11 e elevados a potência de 0.95
* Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result)
* Dica: Utilize a lib Numpy para calcular o desvio padrão
'''

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data