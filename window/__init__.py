from os import system
import colorama

class Window:
    def clear_terminal(self) -> None:
        system('cls')

    def title(self, text: str, space: int, lenght: int) -> None:
        print(colorama.Fore.MAGENTA + '=-=' * lenght)
        print('  ' * space , f'{text}')
        print(colorama.Fore.MAGENTA + '=-=' * lenght)


if __name__ == '__main__':
    board = Window()
    board.title('Amogus', 13, 20)
