from os import system
from time import sleep
from colorama import Fore, Style


class Window:
    def clear_terminal(self) -> None:
        system('cls')

    def delay_prompt(self, delay: float) -> None:
        sleep(delay)

    def title(self, text: str, lenght: int, space: int, dist: int) -> None:
        print(' ' * dist, Fore.MAGENTA + Style.BRIGHT + '=-=' * lenght)
        print(' ' * space , f'{text}')
        print(' ' * dist, Fore.MAGENTA + Style.BRIGHT + '=-=' * lenght)

    def table(self, dist: int) -> None:
        print(' ' * (dist+1), '\033[1m1- Music Converter | 3- Youtube Downloader\n',
              ' ' * dist, '2- Image Converter | 4- Cryptography\033[m\n',
              ' ' * int(dist + (dist/1.4)), '5- Exit')

    def table_yt(self) -> None:
        print('\033[1;33mEscolha a resoulção que você deseja, '
              'digite os numeros ou a própria resolução\n'
              '1: Baixa resolução |  720p, 480p,\n'
              '2: Média resolução |  360p, 240p,\n'
              '3: Alta resolução  |     144p\033[m\n')

    def table_hash(self) -> None:
        print('\033[1;33mQue tipo de criptografia deseja usar?\033[m')
        print(Style.BRIGHT + '1- Hash MD5  | 2- Criptografia única | 3- Sair')

    def sub_table_hash(self):
        print(Fore.YELLOW + Style.BRIGHT + 'Qual modo você deseja usar?')
        print(Style.BRIGHT + '1- Criptografar  | 2- Descriptografar | 3- Reescrever Criptografia')
