from time import sleep
from window import Window
from colorama import init, Fore
init(True)
Window().title(Fore.BLUE + '\033[1mCarregando\033[m', 11, 37, 25)

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
            self.__window.title(Fore.WHITE + 'Mp3 Converter', 11, 35, 25)
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
            if self.__mp3.convert_mp3() != False:
                sleep(3)
                break
            sleep(3)
            self.__window.clear_terminal()

    def init_yt(self):
        def validation() -> str:
            self.__window.title(Fore.WHITE + 'Youtube Downloader', 11, 33, 25)
            link = str(input('Digite o link: ')).strip()
            link_verify = str(input(f'O link "{link}" está correto?[Y/N]: ')).upper().strip()
            
            if link_verify in self.__opc_invalid:
                while True:
                    link = str(input('\nDigite o link: ')).strip()
                    link_verify = str(input(f'O "{link}" está correto?[Y/N]: ')).upper().strip()
                    if link_verify in self.__opc_valid:
                        break

            link_retry = str(input('\nDigite novamente o link: ')).strip()

            while link_retry != link:
                print("\n\033[1;31mOs link's não batem digite corretamente!\033[m")
                link_retry = str(input('Digite o link corretamente: ')).strip()
            return link_retry
        
        def get_video() -> bool:
            while True:
                self.__window.clear_terminal()
                self.__window.title('Youtube Downloader', 11, 33, 25)
                self.__window.table_yt()
                resolution = str(input('>> ')).strip().lower()

                self.__yt = YouDownTube(link)
                get_value = self.__yt.get_request(resolution)
                if get_value != None and get_value is True:
                    print('\033[1;32mO download se encontra na pasta "output"\033[m')
                    sleep(3)
                    self.__window.clear_terminal()
                    return True
                elif get_value is False:
                    sleep(3)
                    self.__window.clear_terminal()
                else:
                    sleep(3)
                    self.__window.clear_terminal()
                    return False
        
        while True:
            link: str = validation()
            
            get_value: bool = get_video()
            if get_value:
                break

    def init_image_converter(self):
        self.__imgc = ImageConverter('aaaa')

    def __home(self):
        self.__window.title(Fore.BLUE + '\033[1mMenu de opções', 11, 35, 25)
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
    main.init_yt()
