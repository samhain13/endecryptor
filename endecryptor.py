"""
EnDecryptor
A simple, salty slide rule encryption and decryption application.
By Arielle B Cruz <http://www.abcruz.com>
Dedicated to the public domain on January 2013.
"""
import string

from pathlib import Path


CHARS = [x for x in string.digits]
CHARS.extend([x for x in string.ascii_letters])
CHARS.extend(['.', ',', '!', '?', ' ', '-', '$', '%'])


class EnDecryptor:
    author = 'arielle.cruz@gmail.com'
    version = '0.9'
    # A list of alphanumeric characters and some punctuation marks:
    mychars = CHARS
    # Encrypt or decrypt mode? We default to encrypt.
    is_encrypt = True
    # The two strings needed for either encryption or decryption.
    string_one = ''
    string_two = ''

    @property
    def result(self) -> str:
        """Returns the result of our application process."""
        return self._do_job()

    def set_strings(self, string_one: str = '', string_two: str = ''):
        """Sets the application target string and salt."""
        # We only accept strings.
        string_one = self._check_string_is_path(string_one)

        if type(string_one) is str and type(string_two) is str:
            self.string_one = string_one
            # The second string (salt) needs to be longer than string one.
            if len(string_one) > len(string_two):
                string_two *= int(len(string_one)/len(string_two)) + 1
            self.string_two = string_two

    def set_to_encrypt(self, is_encrypt: bool = True):
        """Sets the application mode to either encrypt or decrypt."""
        self.is_encrypt = is_encrypt

    def _check_string_is_path(self, string_one) -> str:
        pth = Path(string_one)
        if pth.is_file():
            with open(pth, 'r') as file:
                contents = file.read()
            self.write_to_file = self._create_results_filename(pth)
        else:
            contents = string_one
            self.write_to_file = None
        return contents

    def _create_results_filename(self, source_path: Path) -> Path:
        verb = 'encrypted' if self.is_encrypt else 'decrypted'
        filename = source_path.stem
        parts = list(source_path.parts[:-1])
        parts.append(filename.replace(filename, f'{filename}_{verb}{source_path.suffix}'))
        return Path(*parts)

    def _do_job(self) -> str:
        """Initiates the encrypt/decrypt process."""
        result = []
        # Get the IDs of our strings' characters.
        s0 = self._find_ids(self.string_one)
        s1 = self._find_ids(self.string_two)
        # Begin matching the character IDs against our character list.
        for i in range(len(s0)):
            # Encrypt mode.
            if self.is_encrypt:
                index = s0[i] + s1[i]
                if index >= len(self.mychars):
                    index -= len(self.mychars)
            # Decrypt mode.
            else:
                index = s0[i] - s1[i]
                if index < 0:
                    index += len(self.mychars)
            result.append(self.mychars[index])

        if self.write_to_file is not None:
            with open(self.write_to_file, 'w') as file:
                file.write(''.join(result))
            return str(self.write_to_file)
        else:
            return ''.join(result)

    def _find_ids(self, string_part: str) -> list[int]:
        """Gets the index of each character in string from the mychars list."""
        # We want a non-empty string.
        if not string_part:
            return []
        chars = []  # Dump for indexes of supported characters.
        for i in string_part:
            for j in self.mychars:
                if i == j:
                    chars.append(self.mychars.index(j))
        return chars
