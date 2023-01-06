import os
from PIL import Image
from pathlib import Path
from sys import path
caminho = Path(__file__)
caminho = caminho.parent.parent.parent / 'error_treatment'
caminho = str(caminho).replace('\\', '/')
path.append(caminho)
from tratamento import Treatment


class ImageConverter:
    def __init__(self, name_file_image: str) -> None:        
        #global caminho
        self.__file = name_file_image
        self.__extension: list = ['jpg', 'jpeg', 'png']
        #caminho = caminho[:-15] + 'input/' + name_file_image

    def search_file(self) -> (bool | None):
        search: list = os.listdir('input')
        if self.__file in search:
            self.__extension.remove(f"{self.__file.split('.')[1]}")
        else:
            return ('Sua image não foi encontrada, ' 
                    'verifique se realmente está na pasta "input"')
        
    def converter(self):
        image = Image.open(self.__file)
        image_convertida = image.convert('RGB')
        image_convertida.save(f'{0}')

if __name__ == '__main__':
    imgc = ImageConverter('unnamed.jpg')
    imgc.search_file()
