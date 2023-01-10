from os import system
import colorama

class Window:
    def clear_terminal(self) -> None:
        system('cls')

    def title(self, text: str, lenght: int, space: int, dist: int) -> None:
        print(' ' * dist, colorama.Fore.MAGENTA + '=-=' * lenght)
        print(('' if space == 0 else ' ' * space) , f'{text}')
        print(' ' * dist, colorama.Fore.MAGENTA + '=-=' * lenght)
        
    def table(self, dist: int) -> None:
        print(' ' * (dist+1), '\033[1m1- Music Converter | 3- Youtube Downloader\n',
              ' ' * dist, '2- Image Converter | 4- Cryptography\033[m')


if __name__ == '__main__':
    board = Window()
    board.title('Amogus', 13, 20)
