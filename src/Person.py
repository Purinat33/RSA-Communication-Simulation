# Person class? (Will have keys and stuff generated from RSA)
from encryption import RSA


# Person will have RSA and in addition will have "received_public_keys" that's different from RSA

class Person:
    def __init__(self, username: str) -> None:
        self.username = username
        self.data = RSA(username=username)
        # Will be exchanged with another person later
        self.receipient_keys = (None, None)
        self.receipient_name = ""

    def exchange_key(self, receipient: 'Person'):
        self.receipient_name = receipient.username
        self.receipient_keys = receipient.data.getPublicKeyPair()
        if receipient.receipient_keys == (None, None):
            receipient.exchange_key(self)

    def __str__(self) -> str:
        keyPair = self.data.getPublicKeyPair()
        val = f"{self.username}'s (N, E) pair = ({hex(keyPair[0])}, {hex(keyPair[1])})\n"

        if self.receipient_keys != (None, None) and self.receipient_name != "":
            exchanged = f"Exchanged key with {self.receipient_name}'s (N, E): ({hex(self.receipient_keys[0])}, {hex(self.receipient_keys[1])})"
            val += exchanged

        return val
