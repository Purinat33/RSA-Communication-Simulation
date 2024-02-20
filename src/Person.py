from encryption import RSA


class Person:
    def __init__(self, username: str) -> None:
        self.rsa = RSA()
        self.username = username
        self.__secret_key = self.rsa.get_private_key()
        self.public_key = self.rsa.get_public_key()
        self.paired_Person = None  # Person

    def paired_with(self, pair: "Person"):
        # Exchanging of pair's RSA
        print(
            f"Initiating key exchange between {self.username} and {pair.username}")
        self.paired_Person = pair
        pair.paired_Person = self
        if pair.paired_Person is None:
            pair.pairing(self)

    def __str__(self) -> str:
        val = "----------------------\n"
        val += f"Information for username: {self.username}\n"
        # at least 26 to cut off -- Begin public key -- part
        val += "----------------------\n"
        val += f"Public key: {self.public_key[100:128:2]}\n"
        if self.paired_Person is not None:
            val += "----------------------\n"
            val += f"Paired with: {self.paired_Person.username}\n"
            val += f"With key: {self.paired_Person.public_key[100:128:2]}\n"
        val += "----------------------\n"
        return val
