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


if __name__ == "__main__":
    hash = HashGenerator()
    print(hash.one_time_encryption('secret', 'cript'))
