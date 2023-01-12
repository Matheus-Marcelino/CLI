from PIL.Image import open as Open
from os import listdir, rename, mkdir, remove
from os.path import dirname, realpath


class ImageConverter:
    def __init__(self, name_file_image: str) -> None:        
        self.__file: str = name_file_image
        self.__extension: list = ['jpg', 'jpeg', 'png']
        self.__caminho = str(dirname(realpath(__file__)))[:-31] + 'input/' + name_file_image
        self.__caminho = self.__caminho.replace('/', '\\')

    def __search_file(self) -> (bool | str):
        search: list = listdir('input')
        if self.__file in search:
            self.__file: list = self.__file.split('.')
            self.__extension.remove(f"{self.__file[-1]}")
            return True
        else:
            return ('\033[1;31mSua imagem não foi encontrada, ' 
                    'verifique se realmente está na pasta "input"\033[m')

    def converter(self) -> (bool | None | str):
        def move_image() -> None:
            try:
                rename(self.__file, f'output/{self.__file}')
                print('\033[1;32mImagem convertida, Ela se encontra na pasta output!\033[m')
            except FileNotFoundError:
                mkdir('output')
                move_image()
            except FileExistsError:
                search: list = listdir('output')
                if self.__file in search:
                    remove(self.__file)
                    print('\n\033[1;31mImagem já existente!\033[m')

        def convert() -> (bool | None):
            try:
                self.__file: str = f'{self.__file[0]}.{opc}'
                image = Open(self.__caminho)
                image_convertida = image.convert('RGB')
                image_convertida.save(self.__file)
                move_image()
                return True
            except FileNotFoundError:
                print('\n\033[1;31mO arquivo não se encontra mais na pasta "input"\033[m')

        search: bool | str = self.__search_file()
        if search is True:
            xts: str = ' | '.join(arg for arg in self.__extension)
            while True:
                opc: str = str(input('\nQual tipo de extensão você quer para sua imagem?\n'
                                    f'{xts}\n>> '))
                if opc in xts:
                    break
                else:
                    print('\n\033[1;31mOpção inexistente, escolha uma valida!\033[m')

            data = convert()
            if data is True:
                return True
        else:
            return search
