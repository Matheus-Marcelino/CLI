from time import sleep
from window import Window
from colorama import init, Fore
init(True)
Window().title(Fore.BLUE + '\033[1mCarregando\033[m', 11, 35, 25)

from validation import Calculate_time 
from validation.crypt import HashGenerator
from validation.json_manager import JsonManager
from error_treatment.tratamento import Treatment
from funcionalidades.yt_downloader import YouDownTube
from funcionalidades.mp3_converter import ConverterMp3
from funcionalidades.image_converter import ImageConverter


class Main:
    def __init__(self) -> None:
        self.__window = Window()
        self.__json = JsonManager()
        self.__hash = HashGenerator()
        self.__trat = Treatment()
        self.__opc_valid: tuple[str] = ('Y', 'S', 'YES', 'SIM')
        self.__opc_invalid: tuple[str] =  ('NÃO', 'NAO',  'NO', 'NOT')

    def __home(self):
        self.__window.title(Fore.BLUE + '\033[1mMenu de opções', 11,35, 25)
        self.__window.table(21)
        opc: str = str(input('qual você deseja usar: '))
        match opc:
            case '1':
                pass
                

    @Calculate_time
    def main(self):
        self.__window.clear_terminal()
        while True:
            data = self.__json.read()
            self.__home()
            break
            

if __name__ == '__main__':
    main = Main()
    #main.main()
    main.init_music_converter()
