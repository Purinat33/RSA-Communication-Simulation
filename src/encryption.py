# https://medium.com/@metechsolutions/python-by-examples-rsa-encryption-decryption-d07a226430b4

import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


class RSA:
    def __init__(self, key_size=2048) -> None:
        # Generate a random seed
        random_seed = os.urandom(32)
        # Use the random seed
        backend = default_backend()
        rsa_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=backend
        )
        self.private_key = rsa_private_key
        # Extract the public key
        self.public_key = rsa_private_key.public_key()

    def get_public_key(self):
        # Serialize the public key
        public_key_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return public_key_bytes.decode('utf-8').upper()

    def get_private_key(self):
        # Serialize the private key
        private_key_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        return private_key_bytes.decode('utf-8').upper()
