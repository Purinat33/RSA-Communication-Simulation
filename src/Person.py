from encryption import RSA
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
from binascii import hexlify
from rsa import DecryptionError


class Person:
    def __init__(self, username: str) -> None:
        self.rsa = RSA()
        self.username = username
        self.__private_key = self.rsa.get_private_key()
        self.public_key = self.rsa.get_public_key()
        self.paired_Person = None  # Person
        self.formatted_public_key = self.rsa.get_formatted_key()
        self.private_key_hint = str(self.__private_key)[:19]

    def paired_with(self, pair: "Person"):
        # Exchanging of pair's RSA
        print(
            f"Initiating key exchange between {self.username} and {pair.username}\n")
        self.paired_Person = pair
        pair.paired_Person = self
        if pair.paired_Person is None:
            pair.pairing(self)

    def send(self, message: str) -> bytes:
        # Must always have receiver's public key ready else error
        if self.paired_Person is not None:
            print(f"{self.username} sending data to {self.paired_Person.username}")
            enc_message = self.rsa.encrypt(
                message, self.paired_Person.public_key)
            return enc_message
        else:
            print(f"{self.username} has no recipient. Pair with someone first.\n")
            return

    def decrypt_message(self, encoded_message: bytes) -> str:
        try:
            message = self.rsa.decrypt(encoded_message, self.__private_key)
            return message
        except DecryptionError:
            return f"Decryption failure, invalid PRIVATE KEY 0x{hex(hash(self)).removeprefix('0x').upper()}!"

    def read_raw(self, encoded_message: bytes) -> str:
        return hexlify(encoded_message).decode().upper()

    def __str__(self) -> str:
        val = "----------------------\n"
        val += f"Information for username: {self.username}\n"
        # at least 26 to cut off -- Begin public key -- part
        val += "----------------------\n"
        val += f"Public key: {self.formatted_public_key}\n"
        if self.paired_Person is not None:
            val += "----------------------\n"
            val += f"Paired with: {self.paired_Person.username}\n"
            val += f"With key: {self.paired_Person.formatted_public_key}\n"
        val += "----------------------\n"
        return val
