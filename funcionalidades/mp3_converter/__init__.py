"""
Converta seu mp4 para mp3
        self.__caminho = Path(__file__)
        self.__caminho = self.__caminho.parent.parent.parent / 'input'
        self.__caminho = self.__caminho / f'{self.__path}'
        print(f'\033[1;31m{self.__caminho}\033[m')
"""
from os import rename
from moviepy.editor import VideoFileClip

#Treatment().error_treatment()
class Converter:
    """
    Conversor de extensões
    """
    def __init__(self, name_mp4: str) -> None:
        self.__path = name_mp4
        if '.mp4' not in self.__path:
            self.__path = self.__path + '.mp4'

    def convert_mp3(self, name_your_mp3: str) -> None:
        """Converte seu mp4"""

        if '.mp3' not in name_your_mp3:
            name_your_mp3 = name_your_mp3 + '.mp3'
        
        #@error_treatment.Treatment.error_treatment((OSError), (False))
        def converter() -> None:
            """Função principal para converter"""
            video_clip = VideoFileClip(filename='input/amogus.mp4')
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(name_your_mp3)
            audio_clip.close()
            video_clip.close()

        #@error_treatment.Treatment.error_treatment((FileNotFoundError), (False))
        def move_file() -> None:
            """Função que joga para o output"""
            rename(name_your_mp3, f'output/{name_your_mp3}')

        converter()
        move_file()


if __name__ == '__main__':
    #convertor = Converter('amogus.mp4')
    #convertor.convert_mp3('audio')
    pass