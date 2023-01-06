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
