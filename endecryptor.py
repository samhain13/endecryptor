"""
EnDecryptor
A simple, salty slide rule encryption and decryption application.
By Arielle B Cruz <http://www.abcruz.com>
Dedicated to the public domain on January 2013.
"""
import string


CHARS = [x for x in string.digits]
CHARS.extend([x for x in string.ascii_letters])
CHARS.extend(['.', ',', '!', '?', ' ', '-', '$', '%'])


class EnDecryptor:
    author = 'arielle.cruz@gmail.com'
    version = '0.8'
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
        if type(string_one) is str and type(string_two) is str:
            self.string_one = string_one
            # The second string (salt) needs to be longer than string one.
            if len(string_one) > len(string_two):
                string_two *= int(len(string_one)/len(string_two)) + 1
            self.string_two = string_two

    def set_to_encrypt(self, is_encrypt: bool = True):
        """Sets the application mode to either encrypt or decrypt."""
        self.is_encrypt = is_encrypt

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


# Test and sample commandline usage.
if __name__ == '__main__':
    # Instantiate.
    e = EnDecryptor()
    # Print a greeter.
    print(
        'o-----------oOqpOo\n'
        'Hello, I am Arielle\'s simple Python en|decryptor.\n'
        'Use me to encrypt or decrypt strings of text to use\n'
        'as passwords or just to mask your love letters.\n'
        f'I am currently at version {e.version}, please send your\n'
        f'comments or improvements to {e.author}.\n'
        'oOdbOo-------------o'
    )
    # So we can start over, we'll put everything in a loop.
    running = True
    while running:
        while m := str(input('Decrypt (D) or Encrypt (E) text? ')).lower() \
                not in 'dDeE':
            # Keep asking the user what mode to use; we only want D or E.
            pass
        if m == 'd':
            verb = 'decrypt'
            e.set_to_encrypt(False)
        else:
            verb = 'encrypt'
        print(f'The application has been set to {verb} mode.\n')
        # Ask the user for the text that she wants to encrypt or decrypt
        # as well as the passphrase. Then set both strings.
        str_one = input(f'Please enter the text to {verb}: ')
        str_two = input('Please enter a passphrase: ')
        e.set_strings(str_one, str_two)
        # Tell the EnDecryptor to do its job and show the result to the user.
        print(
            f'Below is the {verb}ed result:\n'
            f'{e.result}\n'
            f'Please keep it in a safe place.'
        )
        # Ask the user if she wants to start over.
        while r := str(input('Would you like to start over (Y|N)? ')).lower() \
                not in 'yYnN':
            if r != 'y':
                running = False  # Kill the app.
                print('  ** Goodbye. **\n')
                quit()
            else:
                print('\n  ** Starting new session. **\n')
