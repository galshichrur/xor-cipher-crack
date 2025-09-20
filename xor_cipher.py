
class XORCipher:

    @staticmethod
    def encrypt_decrypt(plaintext: str, key: str) -> str:
        """Encrypt or decrypt string, returns a string."""
        ciphertext = ""

        for i, pt_char_ascii in enumerate(XORCipher.to_ascii_list(plaintext)):
            ciphertext += chr(pt_char_ascii ^ ord(key[i % len(key)]))

        return ciphertext

    @staticmethod
    def encrypt_decrypt_list(plaintext: list[int], key: str) -> list[int]:
        """Encrypt or decrypt ASCII list, returns ASCII list."""

        return [
            char ^ ord(key[i % len(key)]) for i, char in enumerate(plaintext)
        ]

    @staticmethod
    def to_ascii_list(text: str) -> list[int]:

        return [ord(char) for char in text]

    @staticmethod
    def to_string(ascii_list: list[int]) -> str:

        return ''.join(chr(char) for char in ascii_list)


def test_encrypt_decrypt():
    pt = input("Enter plaintext: ")
    key = input("Enter key: ")
    ciphertext = XORCipher.encrypt_decrypt(pt, key)
    print("Ciphertext: ", ciphertext)
    plaintext = XORCipher.encrypt_decrypt(ciphertext, key)
    print("Plaintext: ", plaintext)
    assert pt == plaintext

def test_encrypt_decrypt_list():
    pt = input("Enter plaintext: ")
    key = input("Enter key: ")
    ciphertext = XORCipher.encrypt_decrypt_list(XORCipher.to_ascii_list(pt), key)
    print("Ciphertext: ", ciphertext)
    plaintext = XORCipher.encrypt_decrypt_list(ciphertext, key)
    print("Plaintext: ", plaintext)
    assert pt == XORCipher.to_string(plaintext)

if __name__ == '__main__':
    test_encrypt_decrypt_list()