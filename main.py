from colorama import init
from window import Window
from error_treatment.tratamento import Treatment 
from validation.crypt import HashGenerator
from validation.json_manager import JsonManager
from funcionalidades.yt_downloader import YouDownTube
from funcionalidades.mp3_converter import ConverterMp3
from funcionalidades.image_converter import ImageConverter
init(True)


class Main:
    def __init__(self) -> None:
        self.__window = Window()
        self.__json = JsonManager()
        self.__hash = HashGenerator()
        self.__yt = YouDownTube()
        self.__mp3 = ConverterMp3()
        self.__imagec = ImageConverter()
        self.__trat = Treatment()

    def main(self):
        while True:
            pass