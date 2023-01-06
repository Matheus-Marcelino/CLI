"""
Converta seu mp4 para mp3
"""
from os import listdir, mkdir, remove, rename
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
        self.__file = name_mp4

    def __checking(self):
        try:
            if self.__file.split('.')[1].replace(' ', '') != ('mp4', 'mkv'):
                return True
        except IndexError:
            self.__file = self.__file + '.mp4'  # Extensão padrão

    def convert_mp3(self, name_your_mp3: str) -> None:
        """Converte seu mp4 para mp3"""

        if self.__checking():
            return '\033[1;31mExtensão não suportada!\033[m' 

        if '.mp3' not in name_your_mp3[-4:]:
            name_your_mp3 = name_your_mp3 + '.mp3'

        @Treatment.error_treatment((OSError, FileNotFoundError),
                                   (True, '\033[1;31mArquivo não encontrado ou pasta não encontrada! '
                                    'Verifique se o arquivo\nestá na pasta "input" ou se a pasta "input" existe.\033[m'))
        def converter() -> bool:
            """Função principal para converter"""
            video_clip = VideoFileClip(filename=f'input/{self.__file}')
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(name_your_mp3)
            audio_clip.close()
            video_clip.close()
            return True

        def move_file() -> None:
            """Função que joga para a pasta output"""
            try:
                rename(name_your_mp3, f'output/{name_your_mp3}')
                print('\033[1;32mMp3 Concluído, Ela se encontra na pasta output!\033[m')
            except FileNotFoundError:
                mkdir('output')
                move_file()
            except FileExistsError:
                search: list = listdir('output')
                if name_your_mp3 in search:
                    remove(name_your_mp3)
                    print('\033[1;31mMp3 já existente!\033[m')

        if converter():
            move_file()


if __name__ == '__main__':
    conversor = Converter('amogus')
    print(conversor.convert_mp3('audio.mp3'))
