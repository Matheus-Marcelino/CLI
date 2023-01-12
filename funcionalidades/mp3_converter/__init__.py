"""
Converta seu mp4 para mp3
"""
from os import listdir, mkdir, remove, rename
from moviepy.editor import VideoFileClip


class ConverterMp3:
    """Conversor de extensões"""
    def __init__(self, name_mp4: str) -> None:
        self.__file = name_mp4

    def __checking(self) -> (bool | None):
        try:
            if self.__file.split('.')[1].replace(' ', '') != 'mp4':
                return True
        except IndexError:
            self.__file = self.__file + '.mp4'  # Extensão padrão

    def convert_mp3(self) -> bool:
        """Converte seu mp4 para mp3"""

        if self.__checking():
            return '\033[1;31mExtensão não suportada!\033[m' 

        def converter() -> bool:
            """Função principal para converter"""
            try:
                video_clip = VideoFileClip(filename=f'input\{self.__file}')
                self.__file = self.__file[:-1] + '3'
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(self.__file)
                audio_clip.close()
                video_clip.close()
                return True
            except (OSError, FileNotFoundError):
                print('\033[1;31mArquivo não encontrado ou pasta não encontrada! '
                      'Verifique se o arquivo\nestá na pasta "input" ou se a pasta "input" existe.\033[m')

        def move_file() -> None:
            """Função que joga para a pasta output"""
            try:
                rename(self.__file, f'output/{self.__file}')
                print('\033[1;32mMp3 Concluído, Ela se encontra na pasta output!\033[m')
            except FileNotFoundError:
                try:
                    mkdir('output')
                    move_file()
                except FileExistsError:
                    pass
            except FileExistsError:
                search: list = listdir('output')
                if self.__file in search:
                    remove(self.__file)
                    print('\033[1;31mMp3 já existente!\033[m')

        if converter():
            move_file()
        else:
            return False
