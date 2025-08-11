from cryptography.fernet import Fernet

def encoding_and_decoding():
    crypto_key = Fernet.generate_key()

    print (crypto_key)

    '''Output:
    
    b'b5DLHxREZaIxQmUU5xNKVR2LgBpK76gJ4aA50JGxsAM='
    '''

    crypto = Fernet(crypto_key)

    text = b'Use cryptograpgy for decoding and encoding'

    encrypted_text = crypto.encrypt(text)

    print (encrypted_text)

    '''Output:
    
    b'gAAAAABiItmgxhIeEVk9B1Q3PpHXxmJpq4SyQggWdidHc1T3s-LJRKCdeieg4IAy81EFAd5JfbQZwJkKQfERSu0WcGUNllyFZzSfntgr0g0S0dMVyyu8W8Y8McwlB1qbKxAxvwC4MgNq''''


    decrypted_text = crypto.decrypt(encrypted_text)

    print (decrypted_text)

    '''Output:
    
    b'Use cryptograpgy for decoding and encoding''''