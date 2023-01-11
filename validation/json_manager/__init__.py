from pathlib import Path
from json import load, dump
from json.decoder import JSONDecodeError


class JsonManager():
    def __init__(self) -> None:
        self.__path = Path(__file__)
        self.__path = str(self.__path.parent.parent.parent / 'data_info.json')
        self.__recovery_data: dict = {
                               "last_boot":{
                                    "last_accessed":{
                                        "date": "dd/mm/aaaa",
                                        "time": "00:00:00"
                                        },
                                    "usage_time": "00:00:00"
                                    },
                                "last_used_feature": "",
                                "message": "error"
                            }

    def read(self) -> dict:
        """Lê o arquivo .json"""
        try:
            with open(self.__path, encoding='utf-8') as file_json:
                obj_json = load(file_json)
        except (FileNotFoundError, JSONDecodeError):
            with open(self.__path, 'w+',encoding='utf-8') as file_error_json:
                self.__recovery_data["message"] = 'error'
                dump(self.__recovery_data, file_error_json, indent=4)

        with open(self.__path, encoding='utf-8') as file_json:
                obj_json = load(file_json)
        return obj_json

    def insert(self, data: dict) -> None:
        """Insere e Atualiza o .json"""
        with open(self.__path, 'w+',encoding='utf-8') as file_json:
            dump(data, file_json, indent=4)


if __name__ == '__main__':
    js = JsonManager()
    js.read()
    """js.insert({
                    "last_boot":{
                        "last_accessed":{
                            "date": "dd/mm/aaaa",
                            "time": "00:00:00"
                            },
                        "usage_time": "00:00:00"
                        },
                    "last_used_feature": "",
                    "message": "error"
                }
            )
    """