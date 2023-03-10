
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from urllib.error import URLError
from os.path import dirname, realpath

class YouDownTube:
    def __init__(self, link: str) -> None:
        self.__link: str = link
        self.__resolutions: tuple[str] = ('720', '480',
                                           '360', '240',
                                           '144')
        self.__caminho: str = dirname(realpath(__file__))[:-29]

    def __capsule(self) -> (bool | None):
        try:
            self.__yt = YouTube(self.__link)
            return True
        except RegexMatchError:
            print('\033[1;31mLink escrito de forma errada\033[m')            

    def get_request(self, resolution: str):
        if not self.__capsule():
            return 'error'

        def validation_input():
            nonlocal resolution
            if 'www.youtube.com' not in self.__link[8:23]:
                return False

            if 'https://www.youtube.com/watch?' not in self.__link[:30]:
                return True

            if resolution in self.__resolutions and resolution[-1] != 'p':
                resolution =  resolution + 'p'

            try:
                match resolution:
                    case '1':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_lowest_resolution()
                    case '2':
                        print('\033[1;32mFazendo download do seu video...\033[m')
                        return self.__yt.streams.get_by_resolution("480p")
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
                        print('\033[1;31mEscolha uma resolu????o v??lida\033[m')
                        return 'invalid_resolution'
            except URLError:
                print('\033[1;31mErro de conex??o ou Verifique o seu link!\033[m')

        def download() -> None:
            self.__yt.download(output_path=self.__caminho + 'output')

        self.__yt = validation_input()
        if self.__yt is True:
            print('\033[1;31mLink Invalido! Escreva-o de maneira certa.\033[m')
            return 'error'

        if self.__yt is False:
            print('\033[1;31mO dominio n??o ?? do youtube!\033[m')
            return "error domain"

        if self.__yt == 'invalid_resolution':
            return False

        if self.__yt is not None:
            download()
            print('\033[1;32mDownload Feito com sucesso!\033[m')
            return True
