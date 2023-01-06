from pytube import YouTube
from pytube.exceptions import RegexMatchError
from urllib.error import URLError
from pathlib import Path
from os import system
from sys import path
caminho = Path(__file__)
caminho = caminho.parent.parent.parent / 'error_treatment'
caminho = str(caminho).replace('\\', '/')
path.append(caminho)
from tratamento import Treatment


class YouDownTube:
    def __init__(self, link: str) -> None:
        self.__link: str = link

    @Treatment.error_treatment(type_of_error=(RegexMatchError), 
                               message=(True, '\033[1;31mLink escrito de forma errada\033[m'))
    def __capsule(self) -> (bool | None):
        self.__yt = YouTube(self.__link)
        return True

    def get_request(self):
        if not self.__capsule():
            return 'error'

        @Treatment.error_treatment(type_of_error=(URLError),
                                   message=(True, '\033[1;31mErro de conexão, '
                                            'Verifique se você está Online!\033[m'))
        def validation_input():
            if 'www.youtube.com' not in self.__link[8:23]:
                return False

            if 'https://www.youtube.com/watch?' not in self.__link[:30]:
                return True

            while True:
                resolution = str(input('Escolha a resoulção que você deseja, '
                                       'digite os numeros ou a própria resolução\n'
                                        '1: Baixa resolução |  720p, 480p,\n'
                                        '2: Média resolução |  360p, 240p,\n'
                                        '3: Alta resolução  |     144p\n'
                                        '>> '))
                if resolution != ('1' or '2' or '3') and resolution[-1] != 'p':
                    resolution =  resolution + 'p'

                match resolution:
                    case '1':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_lowest_resolution()
                    case '2':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('480p')
                    case '3':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_highest_resolution()
                    case '720p':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('720p')
                    case '480p':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('480p')
                    case '360p':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('360p')
                    case '240p':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('240p')
                    case '144p':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution('144p')
                    case _:
                        system('cls')
                        print('\033[1;31mEscolha uma resolução válida\033[m')

        def download() -> None:
            self.__yt.download(output_path=caminho[:-15] + 'output')

        self.__yt = validation_input()
        if self.__yt is True:
            print('\033[1;31mLink Invalido! Escreva-o de maneira certa.\033[m')
        elif self.__yt is False:
            print('\033[1;31mO dominio não é do youtube!\033[m')
        elif self.__yt != None:
            download()
            print('\033[1;32mDownload Feito com sucesso!\033[m')


if __name__ == '__main__':
    yt = YouDownTube('https://www.youtube.com/watch?v=07k3exN1DlI')
    yt.get_request()
