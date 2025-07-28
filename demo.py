from endecryptor import EnDecryptor


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
        mode = str(input('Decrypt (D) or Encrypt (E) text? ')).lower()
        if mode == 'd':
            verb = 'decrypt'
            e.set_to_encrypt(False)
        else:
            verb = 'encrypt'
            e.set_to_encrypt(True)
        print(f'The application has been set to {verb} mode.\n')
        # Ask the user for the text that she wants to encrypt or decrypt
        # as well as the passphrase. Then set both strings.
        str_one = input(f'Please enter the text to {verb}: ')
        str_two = input('Please enter a passphrase: ')
        e.set_strings(str_one, str_two)
        # Tell the EnDecryptor to do its job and show the result to the user.
        print(
            f'Below is the {verb}ed result:\n'
            f'{e.result}\n\n'
        )
        # Ask the user if she wants to start over.
        restart = str(input('Would you like to start over (Y|N)? ')).lower()
        if restart != 'y':
            running = False  # Kill the app.
            print('\n  ** Goodbye. **\n')
        else:
            print('\n  ** Starting new session. **\n')
