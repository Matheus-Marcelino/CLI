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

    def init_music_converter(self):
        while True:
            self.__window.title('Mp3 Converter', 11,35, 25)
            print('\n\033[1;33mCertifique-se que o arquivo esteja na pasta "input"')
            opcion = str(input('Digite o nome do arquivo: '))
            opcion_verify = str(input(f'O nome "{opcion}" está correto?[Y/N]: ')).upper().strip()

            if opcion_verify in self.__opc_invalid:
                while True:
                    opcion = str(input('\nDigite o nome do arquivo: '))
                    opcion_verify = str(input(f'O nome "{opcion}" está correto?[Y/N]: ')).upper().strip()
                    if opcion_verify in self.__opc_valid:
                        break

            opcion_retry = str(input('\nDigite novamente o nome do arquivo: '))

            while opcion_retry != opcion:
                print('\nOs nomes não batem digite corretamente!')
                opcion_retry = str(input('Digite o nome correto do arquivo: '))

            print()
            self.__mp3 = ConverterMp3(opcion_retry)
            self.__mp3.convert_mp3(opcion_retry)
            sleep(3)
            break

    def init_yt(self):
        self.__yt = YouDownTube('aaa')

    def init_image_converter(self):
        self.__imgc = ImageConverter('aaaa')


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
