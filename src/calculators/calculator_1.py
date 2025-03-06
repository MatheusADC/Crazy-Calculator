from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first__process(splited_number)
        return {"result": first_process_result}

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["number"]
        return input_data
    
    def __first__process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part