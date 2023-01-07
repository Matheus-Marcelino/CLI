from pathlib import Path
from json import load, dump
from json.decoder import JSONDecodeError


class JsonManager():
    def __init__(self) -> None:
        self.__path = Path(__file__)
        self.__path = str(self.__path.parent.parent.parent / 'data_info.json')

    def read(self) -> dict:
        try:
            with open(self.__path, encoding='utf-8') as file_json:
                obj_json = load(file_json)
        except (FileNotFoundError, JSONDecodeError):
            with open(self.__path, 'w+',encoding='utf-8') as file_error_json:
                file_error_json.write("""{\n\t"local":"ERROR"\n}""")

        with open(self.__path, encoding='utf-8') as file_json:
                obj_json = load(file_json)
        return obj_json

    def insert(self, data: dict) -> dict:
        with open(self.__path, 'w+',encoding='utf-8') as file_json:
            dump(data, file_json, indent=4)


if __name__ == '__main__':
    js = JsonManager()
    js.insert({"time_used":{
                    "last_accessed": "dd/mm/aaaa",
                    "time_use": "00:00:00"
                },
               "last_accessed_feature": ""
               }
              )
