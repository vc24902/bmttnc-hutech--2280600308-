# cipher/caesar/caesar_cipher.py
from cipher.caesar import ALPHABEST

class CaesarCipher:
    def __init__(self):
        self.alphabest = ALPHABEST

    def encrypt_text(self, text, key):
        # Mã hóa văn bản
        encrypted_text = []
        for letter in text:
            if letter in self.alphabest:
                letter_index = self.alphabest.index(letter)
                encrypted_text.append(self.alphabest[(letter_index + key) % len(self.alphabest)])
            else:
                encrypted_text.append(letter)
        return ''.join(encrypted_text)

    def decrypt_text(self, text, key):
        # Giải mã văn bản
        decrypted_text = []
        for letter in text:
            if letter in self.alphabest:
                letter_index = self.alphabest.index(letter)
                decrypted_text.append(self.alphabest[(letter_index - key) % len(self.alphabest)])
            else:
                decrypted_text.append(letter)
        return ''.join(decrypted_text)
