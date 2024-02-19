# Using RSA from another of my repo: https://github.com/Purinat33/Python-Cryptography-From-Scratch

from random import randint
# https://www.simplilearn.com/tutorials/cryptography-tutorial/rsa-algorithm
# https://www.factors-of.com/prime-numbers-before/Prime-numbers-from-1-to_3000_

prime = [
    1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999,
    3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493
]


# Recursive
# https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/
def hcf(a, b):
    # Everything divides 0
    if (b == 0):
        return a
    return hcf(b, a % b)


class RSA:

    def __init__(self, username="Alice") -> None:
        self.__username = str(username)
        self.__rand_p = randint(0, len(prime))
        self.__rand_q = randint(0, len(prime))
        self.__p = prime[self.__rand_p]
        self.__q = prime[self.__rand_q]
        self.__n = self.__p*self.__q
        self.__tau = ((self.__p - 1) * (self.__q - 1))
        self.__E = self.__genPublicKey(self.__tau)
        self.__D = self.__genPrivateKey(self.__E, self.__tau)

    def __genPublicKey(self, tau: int) -> int:
        # Public Key: E
        # Must be prime
        # 1 < E < self.tau
        # Must not be a factor of tau AKA HCF(E, tau) = 1
        e = 2
        while hcf(e, tau) != 1:
            e = e + 1
        return e

    def __genPrivateKey(self, E: int, tau: int) -> int:
        # Since D*E (mod Tau) = 1
        return pow(E, -1, tau)

    def getPublicKeyPair(self) -> tuple[int, int]:
        return (self.__n, self.__E)

    # Encryption require PUBLIC key of ANOTHER party (both E and N)
    # (message ^ E) mod N
    def encryption(self, plainText: str, N: int, E: int) -> list:
        block_size = 128  # Adjust based on key size and encoding scheme
        cipher = []

        for i in range(0, len(plainText), block_size):
            block = plainText[i:i + block_size]
            encrypted_block = [pow(ord(char), E, N) for char in block]
            cipher.extend(encrypted_block)

        return cipher

    # We have 1 long string of similar-looking value:
    # 3968D834BFE426A0E
    # We want to split them in groups of 2 (if len % 2 == 0 else we just add a 0 at the left most before splitting)
    # The above would become
    # 03 96 8D 83 4B FE 42 6A 0E
    @staticmethod
    def format_text_to_hex(text: list) -> str:
        # Convert each item to hexadecimal and remove the '0x' prefix
        hex_values = [hex(item)[2:].upper() for item in text]

        # Join the hex values into a single string
        hex_string = ''.join(hex_values)

        # If the length is odd, add a '0' at the left most
        if len(hex_string) % 2 != 0:
            hex_string = '0' + hex_string

        # Split the string into groups of 2 characters
        formatted_string = ' '.join([hex_string[i:i+2]
                                    for i in range(0, len(hex_string), 2)])

        return formatted_string

    def decryption(self, encrypted_values: list) -> str:
        decrypted_blocks = []

        for value in encrypted_values:
            decrypted_char = pow(value, self.__D, self.__n)
            decrypted_blocks.append(chr(decrypted_char))

        return ''.join(decrypted_blocks)

    def __str__(self) -> str:
        p = format(self.__p, '02X').zfill(10)
        q = format(self.__q, '02X').zfill(10)
        n = format(self.__n, '02X').zfill(10)
        tau = format(self.__tau, '02X').zfill(10)
        E = format(self.__E, '02X').zfill(10)
        D = format(self.__D, '02X').zfill(10)

        val = "--------------------------------\n"
        val += f"RSA Information for {self.__username}\n"
        val += f"P:\t\t {p[:2]} {p[2:4]} {p[4:6]} {p[6:8]} {p[8:10]}\n"
        val += f"Q:\t\t {q[:2]} {q[2:4]} {q[4:6]} {q[6:8]} {q[8:10]}\n"
        val += f"N:\t\t {n[:2]} {n[2:4]} {n[4:6]} {n[6:8]} {n[8:10]}\n"
        val += f"Tau(N):\t\t {tau[:2]} {tau[2:4]} {tau[4:6]} {tau[6:8]} {tau[8:10]}\n"
        val += f"Public Key E:\t {E[:2]} {E[2:4]} {E[4:6]} {E[6:8]} {E[8:10]}\n"
        val += f"Private Key D:\t {D[:2]} {D[2:4]} {D[4:6]} {D[6:8]} {D[8:10]}\n"
        val += "--------------------------------\n"

        return val
