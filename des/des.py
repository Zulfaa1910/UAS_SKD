from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class Encryption:
    def __init__(self, key, block_size):
        self.key = key
        self.block_size = block_size

    def encrypt(self, plain_text):
        raise NotImplementedError("Subclasses must implement this method")

    def decrypt(self, encrypted_text):
        raise NotImplementedError("Subclasses must implement this method")


class DESEncryption(Encryption):
    def __init__(self, key):
        super().__init__(key, block_size=8)
        self.des = DES.new(self.key, DES.MODE_ECB)

    def encrypt(self, plain_text):
        padded_text = pad(plain_text.encode(), self.block_size)
        encrypted_text = self.des.encrypt(padded_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = self.des.decrypt(encrypted_text)
        return unpad(decrypted_text, self.block_size).decode()


# Example usage:
if __name__ == "__main__":
    # Create an instance of DESEncryption
    des_encryptor = DESEncryption(key=b'inikunci')

    # Encrypt and decrypt using DES
    plain_text = "zulfaaulia"
    encrypted_text = des_encryptor.encrypt(plain_text)
    decrypted_text = des_encryptor.decrypt(encrypted_text)

    # Print results
    print("Plain Text: ", plain_text)
    print("Encrypted Text: ", encrypted_text)
    print("Decrypted Text: ", decrypted_text)
