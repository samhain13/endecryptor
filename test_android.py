"""
    Use with Scripting Layer for Android (SL4A).
"""
from android import Android
from endecryptor import EnDecryptor

# Instantiate our main classes.
droid = Android()
endec = EnDecryptor()

def get_user_mode():
    """Asks the user whether to use Encrypt or Decrypt mode."""
    droid.dialogCreateAlert("Set Application Mode")
    droid.dialogSetItems(["Encrypt", "Decrypt"])
    droid.dialogShow()
    if droid.dialogGetResponse().result["item"] == 1:
        return False, "decrypt"
    else:
        return True, "encrypt"

def show_user_result(result_string):
    """Shows the user the result of the encryption/decryption process and
    lets the user save that result onto the clipboard for later use.
    """
    droid.dialogCreateAlert("Endecryptor Result", result_string)
    droid.dialogSetPositiveButton("Copy")
    droid.dialogSetNegativeButton("Exit")
    droid.dialogShow()
    if droid.dialogGetResponse().result["which"] == "positive":
        droid.setClipboard(result_string)
        droid.makeToast("Copied to Clipboard.")

# Ask the user for the mode.
mod_bool, mod_str = get_user_mode()
# Ask the user for the string to encrypt/decrypt.
string_one = droid.dialogGetInput("EnDecryptor", "String to %s:" % mod_str).result
# Ask the user for the passphrase.
String_two = droid.dialogGetInput("EnDecryptor", "Passphrase:").result
# Set the strings.
endec.set_strings(str(string_one), str(string_two))
# Get and show the result.
show_user.result(endec.get_result())

