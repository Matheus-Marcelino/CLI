from window import Window
from colorama import init, Fore, Style
init(True)
Window().title(Fore.BLUE + '\033[1mCarregando\033[m', 11, 37, 25)

from datetime import datetime
from validation import Calculate_time 
from validation.crypt import HashGenerator
from validation.json_manager import JsonManager
from funcionalidades.yt_downloader import YouDownTube
from funcionalidades.mp3_converter import ConverterMp3
from funcionalidades.image_converter import ImageConverter


class Main:
    """Junção de todas as funções para rodar o programa"""
    def __init__(self) -> None:
        self.__window = Window()
        self.__hash = HashGenerator()
        self.__json = JsonManager()
        self.__data: dict = self.__json.read()
        self.__opc_valid: tuple[str] = ('Y', 'S', 'YES', 'SIM')
        self.__opc_invalid: tuple[str] =  ('NÃO', 'NAO',  'NO', 'NOT')

    def __init_music_converter(self) -> None:
        """Inicia o music converter"""
        def validation():
            """Etapa de validação"""
            self.__window.title(Style.BRIGHT + 'Mp3 Converter', 11, 35, 25)
            print('\n\033[1;33mCertifique-se que o arquivo esteja na pasta "input" '
                  'e de colocar a extensão correta\033[m')
            file = str(input('Digite o nome do arquivo: '))
            file_verify = str(input(f'O nome "{file}" está correto?[Y/N]: ')).upper().strip()

            if file_verify in self.__opc_invalid:
                while True:
                    file = str(input('\nDigite o nome do arquivo: '))
                    file_verify = str(input(f'O nome "{file}" está correto?[Y/N]: ')).upper().strip()
                    if file_verify in self.__opc_valid:
                        break

            file_retry = str(input('\nDigite novamente o nome do arquivo: '))

            while file_retry != file:
                print('\nOs nomes não batem digite corretamente!')
                file_retry = str(input('Digite o nome correto do arquivo: '))
            return file_retry

        while True:
            get_value: str = validation()

            print()
            self.__mp3 = ConverterMp3(get_value)
            if self.__mp3.convert_mp3() is not False:
                self.__window.delay_prompt(3)
                self.__window.clear_terminal()
                break
            self.__window.delay_prompt(3)
            self.__window.clear_terminal()

    def __init_yt_downloader(self) -> None:
        """Inicia o youtube downloader"""
        def validation() -> str:
            """Etapa de validação"""
            self.__window.title(Style.BRIGHT + 'Youtube Downloader', 11, 33, 25)
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
            """Inicia a procura e o download do video"""
            while True:
                self.__window.clear_terminal()
                self.__window.title('Youtube Downloader', 11, 33, 25)
                self.__window.table_yt()
                resolution = str(input('>> ')).strip().lower()

                self.__yt = YouDownTube(link)
                get_value = self.__yt.get_request(resolution)
                if get_value is not None and get_value is True:
                    print('\033[1;32mO download se encontra na pasta "output"\033[m')
                    self.__window.delay_prompt(3)
                    self.__window.clear_terminal()
                    return True

                if get_value is False:
                    self.__window.delay_prompt(3)
                    self.__window.clear_terminal()
                else:
                    self.__window.delay_prompt(3)
                    self.__window.clear_terminal()
                    return False

        while True:
            link: str = validation()

            get_value: bool = get_video()
            if get_value:
                break

    def __init_image_converter(self) -> None:
        def validation() -> str:
            """Etapa de validação"""
            self.__window.title(Style.BRIGHT + 'Mp3 Converter', 11, 35, 25)
            print('\n\033[1;33mCertifique-se que o arquivo esteja na pasta "input" '
                  'e de colocar a extensão correta\033[m')
            file = str(input('Digite o nome do arquivo: '))
            file_verify = str(input(f'O nome "{file}" está correto?[Y/N]: ')).upper().strip()

            if file_verify in self.__opc_invalid:
                while True:
                    file = str(input('\nDigite o nome do arquivo: '))
                    file_verify = str(input(f'O nome "{file}" está correto?[Y/N]: ')).upper().strip()
                    if file_verify in self.__opc_valid:
                        break

            file_retry = str(input('\nDigite novamente o nome do arquivo: '))

            while file_retry != file:
                print('\nOs nomes não batem digite corretamente!')
                file_retry = str(input('Digite o nome correto do arquivo: '))
            return file_retry

        while True:
            get_value: str = validation()

            self.__imgc = ImageConverter(get_value)

            verify: bool | str | None = self.__imgc.converter()
            if isinstance(verify, str):
                print(verify)
                self.__window.delay_prompt(2)
                self.__window.clear_terminal()
                continue
            if verify is True:
                self.__window.delay_prompt(3)
                self.__window.clear_terminal()
                break

            self.__window.delay_prompt(2)
            self.__window.clear_terminal()

    def __init_hash_generator(self) -> None:
        while True:
            self.__window.title(Style.BRIGHT + 'Hash Generator', 11, 35, 25)
            self.__window.table_hash()
            type_encrypt = str(input('Escolha: '))
            match type_encrypt:
                case '1':
                    text = str(input('\nDigite o seu texto: '))
                    hash_md5: str = self.__hash.md5_hash(text)
                    print(f'O seu hash foi: {Fore.GREEN + hash_md5}')
                    print(Fore.YELLOW + Style.BRIGHT +'O seu hash se '
                          'encontra no arquivo "crypto.txt" na pasta "output"')
                    self.__hash.to_output(hash_md5, 'MD5_Hash')
                    self.__window.delay_prompt(3.9)
                    self.__window.clear_terminal()

                case '2':
                    while True:
                        self.__window.clear_terminal()
                        self.__window.title(Style.BRIGHT + 'Criptografia única', 11, 33, 25)
                        self.__window.sub_table_hash()
                        single_crypto = str(input('Qual modo você deseja usar: '))
                        match single_crypto:
                            case '1':
                                text = str(input('\nDigite o seu texto: '))
                                text = self.__hash.one_time_encryption(text, 'encrypt')
                                print(Style.BRIGHT + f'A sua criptografia é: {Fore.GREEN + text}')
                                print(Fore.YELLOW + Style.BRIGHT +'A sua criptografia se '
                                      'encontra no arquivo "crypto.txt" na pasta "output"')
                                self.__hash.to_output(text, 'Single_Crypto - Encrypt')
                                self.__window.delay_prompt(3.9)
                                self.__window.clear_terminal()
                                break

                            case '2':
                                text = str(input('\nDigite o seu texto: '))
                                text = self.__hash.one_time_encryption(text, 'decrypt')
                                if text != '':
                                    print(Style.BRIGHT + f'A sua descriptografia é: {Fore.GREEN + text}')
                                    print(Fore.YELLOW + Style.BRIGHT +'A sua descriptografia se '
                                      'encontra no arquivo "crypto.txt" na pasta "output"')
                                    self.__hash.to_output(text, 'Single_Crypto - Decrypt')
                                    self.__window.delay_prompt(3.9)
                                else:
                                    print(Fore.RED + Style.BRIGHT + 'Esse texto não bate com a criptografia!')
                                    self.__window.delay_prompt(2)
                                self.__window.clear_terminal()
                                break

                            case '3':
                                self.__hash.one_time_encryption(None, 'rewrite')
                                print('\033[1;33mA sua criptografia mudou! qualquer texto que você tenha\n'
                                      'criptografado anteriormente não será mais descriptografado\033[m')
                                self.__window.delay_prompt(4.3)
                                self.__window.clear_terminal()

                            case _:
                                print(Fore.RED +'Escolha uma opção correta!')
                                self.__window.delay_prompt(2)
                case '3':
                    self.__window.clear_terminal()
                    break

                case _:
                    print(Fore.RED + 'Escolha uma opção correta!')
                    self.__window.delay_prompt(1.3)
                    self.__window.clear_terminal()

    def __home(self) -> (bool | None):
        """main menu"""
        def auxiliary(feature: str) -> None:
            self.__data["last_used_feature"] = feature
            print(Fore.GREEN + Style.BRIGHT + "Entrando...")
            self.__window.delay_prompt(1.5)
            self.__window.clear_terminal()

        def get_hour_and_date() -> tuple:
            CALENDAR = datetime.today()
            CURRENT_DATE: str = CALENDAR.strftime('%d/%m/%Y')
            HOUR: str = CALENDAR.strftime('%H:%M:%S')
            return (CURRENT_DATE, HOUR)

        self.__window.title(Fore.BLUE + '\033[1mMenu de opções', 11, 35, 25)
        self.__window.table(21)
        opc: str = str(input('qual você deseja usar: '))
        match opc:
            case '1':
                auxiliary("music_converter")
                self.__init_music_converter()
            case '2':
                auxiliary("image_converter")
                self.__init_image_converter()
            case '3':
                auxiliary("yt_downloader")
                self.__init_yt_downloader()
            case '4':
                auxiliary("hash_generator")
                self.__init_hash_generator()
            case '5':
                CURRENT_DATE: tuple = get_hour_and_date()
                self.__data["last_boot"]["last_accessed"]["date"] = CURRENT_DATE[0]
                self.__data["last_boot"]["last_accessed"]["time"] = CURRENT_DATE[1]
                if self.__data["message"] == "error":
                    self.__data["message"] = 'normal'
                return True

    @Calculate_time
    def main(self) -> tuple:
        """Inicia o código"""
        while True:
            try:
                self.__window.clear_terminal()
                home = self.__home()
                if home:
                    return self.__data
            except KeyboardInterrupt:
                return self.__data

if __name__ == '__main__':
    main = Main()
    DATA: dict = main.main()
    HOUR: str = str(DATA[1])[:7]
    DATA[0]["last_boot"]["usage_time"] = HOUR
    JsonManager().insert(DATA[0])
