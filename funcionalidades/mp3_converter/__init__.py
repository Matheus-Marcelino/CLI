"""
Converta seu mp4 para mp3
"""
from os import mkdir, rename
from moviepy.editor import VideoFileClip
from pathlib import Path
from sys import path
caminho = Path(__file__)
caminho = caminho.parent.parent.parent / 'error_treatment'
caminho = str(caminho).replace('\\', '/')
path.append(caminho)
from tratamento import Treatment


class Converter:
    """Conversor de extensões"""
    def __init__(self, name_mp4: str) -> None:
        self.__path = name_mp4
        if '.mp4' not in self.__path:
            self.__path = self.__path + '.mp4'

    def convert_mp3(self, name_your_mp3: str) -> None:
        """Converte seu mp4 para mp3"""

        if '.mp3' not in name_your_mp3:
            name_your_mp3 = name_your_mp3 + '.mp3'

        @Treatment.error_treatment((OSError, FileNotFoundError),
                                   (True, '\033[1;31mArquivo não encontrado ou pasta não encontrada! '
                                    'Verifique se o arquivo está na pasta "input" ou se a pasta "input" existe.\033[m'))
        def converter() -> bool:
            """Função principal para converter"""
            video_clip = VideoFileClip(filename='input/amogus.mp4')
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(name_your_mp3)
            audio_clip.close()
            video_clip.close()
            return True

        def move_file() -> None:
            """Função que joga para o output"""
            try:
                rename(name_your_mp3, f'output/{name_your_mp3}')
            except FileNotFoundError:
                mkdir('output')
                move_file()

        if converter():
            move_file()


if __name__ == '__main__':
    convertor = Converter('amogus.mp4')
    convertor.convert_mp3('audio')
