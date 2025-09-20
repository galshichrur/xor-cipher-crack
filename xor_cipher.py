
class XORCipher:

    @staticmethod
    def encrypt_decrypt(plaintext: str, key: str) -> str:

        ciphertext = ""
        key_index = 0

        for pt_char_ascii in XORCipher.to_ascii_list(plaintext):
            ciphertext += chr(pt_char_ascii ^ ord(key[key_index % len(key)]))
            key_index += 1

        return ciphertext

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


if __name__ == '__main__':
    test_encrypt_decrypt()