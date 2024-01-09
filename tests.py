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
        result = e.get_result()
        self.assertEqual(ENCRYPTED_TEXT, result)

    def test_encrypt_short_pass_phrase_success(self):
        e = EnDecryptor()
        e.set_strings(PLAIN_TEXT, PASSPHRASE_SHORT)
        result = e.get_result()
        self.assertEqual(ENCRYPTED_TEXT_SHORT, result)

    def test_decrypt_success(self):
        e = EnDecryptor()
        e.set_to_encrypt(False)
        e.set_strings(ENCRYPTED_TEXT, PASSPHRASE)
        result = e.get_result()
        self.assertEqual(PLAIN_TEXT, result)

    def test_decrypt_short_pass_phrase_success(self):
        e = EnDecryptor()
        e.set_to_encrypt(False)
        e.set_strings(ENCRYPTED_TEXT_SHORT, PASSPHRASE_SHORT)
        result = e.get_result()
        self.assertEqual(PLAIN_TEXT, result)
