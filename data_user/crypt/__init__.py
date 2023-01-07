from os import mkdir
from os.path import dirname, realpath, exists
from hashlib import md5
from random import choice
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


class HashGenerator:
    def generator_token(self, complexidade: int) -> str:
        token = ''.join(choice(ascii_lowercase + ascii_uppercase + digits)for _ in range(int(complexidade)))
        return token

    def md5_hash(self, text: str) -> str:
        """Codifica seu texto para um hash MD5"""
        encoded = text.encode('utf-8')
        text: str = md5(encoded).hexdigest()
        return text

    def one_time_encryption(self, text: str, type: str) -> str:
        def save_path() -> None:
            """Cria o arquivo com a criptografia própria"""
            def auxiliar() -> None:  # escreve o arquvio na primeira inicialização
                with open(f'{path}\coden\key.txt', 'w+', encoding='utf-8') as file:
                    for digito in digits:
                        file.write(f'{digito}={self.generator_token(complexidade)}\n')
                    for letra in LETTERS:
                        file.write(f'{letra}={self.generator_token(complexidade)}\n')
                    for symbol in punctuation:
                        file.write(f'{symbol}={self.generator_token(complexidade)}\n')



if __name__ == "__main__":
    hash = HashGenerator()
    print(hash.one_time_encryption('secret', 'cript'))
