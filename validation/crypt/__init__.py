"""Hash Generator"""
from os import mkdir
from os.path import dirname, realpath, exists
from hashlib import md5
from random import choice
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


class HashGenerator:
    def generator_token(self, complexidade: int) -> str:
        """Gera um token"""
        token = ''.join(choice(ascii_lowercase + ascii_uppercase + digits)for _ in range(int(complexidade)))
        return token

    def md5_hash(self, text: str) -> str:
        """Codifica seu texto para um hash MD5"""
        encoded = text.encode('utf-8')
        text: str = md5(encoded).hexdigest()
        return text

    def one_time_encryption(self, text: str | None, encryption_type: str) -> str:
        """Criptografia unica, nenhuma pessoa vai ter a mesma criptografia que a sua"""
        def save_path() -> None:
            """Cria o arquivo com a criptografia própria"""
            def auxiliar() -> None:  # escreve o arquvio na primeira inicialização
                """Auxiliar"""
                with open(f'{path}\coden\key.txt', 'w+', encoding='utf-8') as file:
                    for digito in digits:
                        file.write(f'{digito}={self.generator_token(complexidade)}\n')
                    for letra in LETTERS:
                        file.write(f'{letra}={self.generator_token(complexidade)}\n')
                    for symbol in punctuation:
                        file.write(f'{symbol}={self.generator_token(complexidade)}\n')

            def conjunto() -> None:  # reescreve o arquivo quando acionado novamente
                """Auxiliar"""
                file.seek(0, 0)
                for digito in digits:
                    file.write(f'{digito}={self.generator_token(complexidade)}\n')
                for letra in LETTERS:
                    file.write(f'{letra}={self.generator_token(complexidade)}\n')
                for symbol in punctuation:
                    file.write(f'{symbol}={self.generator_token(complexidade)}\n')

            if not exists(f'{path}\coden'):
                mkdir(f'{path}\coden')
                auxiliar()
            else:
                try:
                    with open(f'{path}\coden\key.txt', 'r+', encoding='utf-8') as file:
                        file.truncate(0)
                        conjunto()
                except FileNotFoundError:
                    auxiliar()

        def encrypt(text: str) -> str:
            """Criptografa qualquer texto"""
            separador = []
            criptografado = ''

            def main() -> str:
                """Criptografador"""
                nonlocal criptografado
                with open(f'{path}\coden\key.txt', 'r', encoding='utf-8') as file:
                    for letra in text:
                        file.seek(0,0)
                        for cripto in file:
                            validacao = letra in cripto[:1]
                            if validacao:
                                separador.append(cripto[2:complexidade+2])
                                criptografado = ''.join(separador)
                                break
                    return criptografado

            try:
                return main()
            except FileNotFoundError:
                save_path()
                return main()

        def decrypt(text: str) -> str:
            """Descriptografa o um texto criptografado com a sua key"""
            text = text.strip(' ')
            agrupador = []
            separador = descriptografado = ''
            mem, mem2 = 0, complexidade
            # {mem, mem2} usado para avançar pela criptografia no tamanho da complexidade
            def main():
                """Descriptografador"""
                nonlocal mem, mem2, separador, descriptografado
                with open(f'{path}\coden\key.txt', 'r', encoding='utf-8') as file:
                    while True:
                        file.seek(0)
                        separador = text[mem:mem2]
                        mem += complexidade
                        mem2 += complexidade
                        if separador != '':
                            for cripto in file:
                                validacao = separador in cripto[2:]
                                if validacao:
                                    agrupador.append(cripto[:1])
                                    descriptografado = ''.join(agrupador)
                                    break
                        else:
                            break
                    return descriptografado

            try:
                return main()
            except FileNotFoundError:
                save_path()
                return main()

        path: str = dirname(realpath(__file__))
        LETTERS = ' AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        complexidade = 10

        if not exists(f'{path}\coden'):
            save_path()

        if encryption_type == 'encrypt' and text is not None:
            return encrypt(text)
        if encryption_type == 'decrypt' and text is not None:
            return decrypt(text)
        if encryption_type == 'rewrite' and text is None:
            save_path()

    def to_output(self, text: str, encryption_type: str) -> None:
        """Move o arquivo para pasta output"""
        out_path = str(dirname(realpath(__file__)))[:-16]

        if not exists(f'{out_path}\output'):
            mkdir(f'{out_path}\output')

        if not exists(f'{out_path}\output\crypto.txt'):
            with open(f'{out_path}\output\crypto.txt', 'w+', encoding='utf-8') as file_c:
                file_c.write(f'{encryption_type}: {text}\n')
        else:
            with open(f'{out_path}\output\crypto.txt', 'a', encoding='utf-8') as file_c:
                file_c.write(f'{encryption_type}: {text}\n')
