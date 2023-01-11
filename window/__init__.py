from os import system
from colorama import Fore

class Window:
    def clear_terminal(self) -> None:
        system('cls')

    def title(self, text: str, lenght: int, space: int, dist: int) -> None:
        print(' ' * dist, Fore.MAGENTA + '=-=' * lenght)
        print(('' if space == 0 else ' ' * space) , f'{text}')
        print(' ' * dist, Fore.MAGENTA + '=-=' * lenght)
        
    def table(self, dist: int) -> None:
        print(' ' * (dist+1), '\033[1m1- Music Converter | 3- Youtube Downloader\n',
              ' ' * dist, '2- Image Converter | 4- Cryptography\033[m\n',
              ' ' * int(dist + (dist/1.4)), '5- Exit')
        
    def table_yt(self) -> None:
        print('\033[1;31mEscolha a resoulção que você deseja, '
              'digite os numeros ou a própria resolução\n'
              '1: Baixa resolução |  720p, 480p,\n'
              '2: Média resolução |  360p, 240p,\n'
              '3: Alta resolução  |     144p\033[m\n')
