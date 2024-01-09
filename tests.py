from unittest import TestCase

from endecryptor import EnDecryptor


PASSPHRASE = 'this is a passphrase that is longer than the plain text'
PASSPHRASE_SHORT = 'short'
ENCRYPTED_TEXT = '2vDNkbopotS6VQlvOmTMlW'
ENCRYPTED_TEXT_SHORT = '1vJMRldRF.VdRPpGEAS,RK'
PLAIN_TEXT = 'Hello, text to encrypt'


class TestEndecryptor(TestCase):

    def test_encrypt_success(self):
        e = EnDecryptor()
        e.set_strings(PLAIN_TEXT, PASSPHRASE)
        self.assertEqual(ENCRYPTED_TEXT, e.result)

    def test_encrypt_short_pass_phrase_success(self):
        e = EnDecryptor()
        e.set_strings(PLAIN_TEXT, PASSPHRASE_SHORT)
        self.assertEqual(ENCRYPTED_TEXT_SHORT, e.result)

    def test_decrypt_success(self):
        e = EnDecryptor()
        e.set_to_encrypt(False)
        e.set_strings(ENCRYPTED_TEXT, PASSPHRASE)
        self.assertEqual(PLAIN_TEXT, e.result)

    def test_decrypt_short_pass_phrase_success(self):
        e = EnDecryptor()
        e.set_to_encrypt(False)
        e.set_strings(ENCRYPTED_TEXT_SHORT, PASSPHRASE_SHORT)
        self.assertEqual(PLAIN_TEXT, e.result)
