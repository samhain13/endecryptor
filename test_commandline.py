#!/usr/bin/env python
"""
    EnDecryptor test for command line use.
"""
from endecryptor import EnDecryptor

# Instantiate.
e = EnDecryptor()
# Print a greeter.
print """
o-----------oOqpOo
Hello, I am Arielle\'s simple Python en|decryptor.
Use me to encrypt or decrypt strings of text to use
as passwords or just to mask your love letters.
I am currently at version %s, please send your
comments or improvements to %s.
                              oOdbOo-------------o
""" % (e.version, e.author)
# So we can start over, we'll put everything in a loop.
running = True
while running:
    # Ask the user whether she wants to encrypt or decrypt text.
    m = "x"
    while m not in "dDeE":
        m = str(raw_input("Decrypt (D) or Encrypt (E) text? ")).lower()
    if m == "d":
        verb = "decrypt"
        e.set_to_encrypt(False)
    else:
        verb = "encrypt"
    print "The application has been set to %s mode.\n" % verb
    # Ask the user for the text that she wants to encrypt or decrypt
    # as well as the passphrase. Then set both strings.
    string_one = str(raw_input("Please enter the text to %s: " % verb))
    string_two = str(raw_input("Please enter a passphrase: "))
    e.set_strings(string_one, string_two)
    # Tell the EnDecryptor to do its job and show the result to the user.
    result = e.get_result()
    print """
Below is the %sed result:

      %s

Please keep it in a safe place.
""" % (verb, result)
    # Ask the user if she wants to start over.
    r = "x"
    while r not in "yYnN":
        r = str(raw_input("Would you like to start over (Y|N)? ")).lower()
        if r != "y":
            running = False  # Kill the app.
            print "  ** Goodbye. **\n"
            quit()
        else:
            print "\n  ** Starting new session. **\n"
