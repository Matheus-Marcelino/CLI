from os import listdir, rename, mkdir, remove, system
from PIL import Image
from pathlib import Path
from sys import path
caminho = Path(__file__)
caminho = caminho.parent.parent.parent / 'error_treatment'
caminho = str(caminho).replace('\\', '/')
path.append(caminho)
from tratamento import Treatment


class ImageConverter:
    def __init__(self, name_file_image: str) -> None:        
        global caminho
        self.__file = name_file_image
        self.__extension: list = ['jpg', 'jpeg', 'png']
        self.__caminho = caminho[:-15] + 'input/' + name_file_image

    def search_file(self) -> (bool | None):
        search: list = listdir('input')
        if self.__file in search:
            self.__file: list = self.__file.split('.')
            self.__extension.remove(f"{self.__file[1]}")
        else:
            return ('\033[1;31mSua imagem não foi encontrada, ' 
                    'verifique se realmente está na pasta "input"\033[m')
        
    def converter(self):
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
                    print('\033[1;31mImagem já existente!\033[m')
                
        @Treatment.error_treatment(self, type_of_error=(FileNotFoundError),
                                   message=(True, '\033[1;31mO arquivo não se encontra mais na pasta "input"\033[m'))
        def convert() -> None:
            self.__file: str = f'{self.__file[0]}.{opc}'
            image = Image.open(self.__caminho)
            image_convertida = image.convert('RGB')
            image_convertida.save(self.__file)
            move_image()

        xts: str = ' | '.join(arg for arg in self.__extension)
        while True:
            opc: str = str(input('Qual tipo de extensão você quer para sua imagem?\n'
                                 f'{xts}\n>> '))
            if opc in xts:
                break
            else:
                system('cls')
                print('\033[1;31mOpção inexistente, escolha uma valida!\033[m')

        convert()


if __name__ == '__main__':
    imgc = ImageConverter('unnamed.jpg')
    imgc.search_file()
    imgc.converter()
