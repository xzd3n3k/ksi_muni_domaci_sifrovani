def encode(n: int, plain_text: str) -> str:     # vraci ciphertext typu String

    parts = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
    parts_reversed = []

    for part in parts:
        text = ''

        for x in range(len(part)-1, -1, -1):
            text += part[x]

        parts_reversed.append(text)

    return ''.join(parts_reversed)

def decode(n: int, cipher_text: str) -> str:    # vraci plaintext typu String
    parts = [cipher_text[i:i + n] for i in range(0, len(cipher_text), n)]
    parts_reversed = []

    for part in parts:
        text = ''

        for x in range(len(part) - 1, -1, -1):
            text += part[x]

        parts_reversed.append(text)

    return ''.join(parts_reversed)

# Testy:
print(encode(3, "Ahoj"))    # ohAj
print(encode(2, "Ahoj"))    # hAjo
print(encode(10, "Ahoj"))   # johA
print(encode(3, "12345"))   # 32154
print(encode(5, "komunikace"))  # numokecaki
print(decode(2, "hAjo"))    # Ahoj
print(decode(5, "rgorpavomain"))    # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane