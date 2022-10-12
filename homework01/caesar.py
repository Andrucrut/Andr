def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    new_word = []  # новое слово
    ciphertext = ""  # новая буква
    for i in plaintext:  # i буква
        if ord(i) >= 65 and ord(i) <= 90:  # от A до Z
            ciphertext = chr(
                (((ord(i) - 65) + shift) % 26) + 65
            )  # %26 чтобы у нас послдний символ был тем что надо
            new_word.append(ciphertext)
        elif ord(i) >= 97 and ord(i) <= 122:  # проверка маленьких букв
            ciphertext = chr((((ord(i) - 97) + shift) % 26) + 97)
            new_word.append(ciphertext)
        else:
            new_word.append(i)
    return "".join(new_word)  # возвращение в качестве строки


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    new_word = []
    new_letter = ""
    for i in ciphertext:
        if ord(i) >= 65 and ord(i) <= 90:
            new_letter = chr((((ord(i) - 65) - shift) % 26) + 65)
            new_word.append(new_letter)
        elif ord(i) >= 97 and ord(i) <= 122:
            new_letter = chr((((ord(i) - 97) - shift) % 26) + 97)
            new_word.append(new_letter)
        else:
            new_word.append(i)
    return "".join(new_word)

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    new_word = []
    ciphertext = ''
    for i in plaintext:
        if ord(i) >= 65 and ord(i) <= 90:
            ciphertext= chr((((ord(i) - 65) + shift) % 26) + 65)
            new_word.append(ciphertext)
        elif ord(i) >= 97 and ord(i) <= 122:
            ciphertext = chr((((ord(i) - 97) + shift) % 26) + 97)
            new_word.append(ciphertext)
        else:
            new_word.append(i)
    return "".join(new_word)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    new_word = []
    new_letter = ''
    for i in ciphertext:
        if ord(i) >= 65 and ord(i) <= 90:
            new_letter = chr((((ord(i) - 65) - shift) % 26) + 65)
            new_word.append(new_letter)
        elif ord(i) >= 97 and ord(i) <= 122:
            new_letter = chr((((ord(i) - 97) - shift) % 26) + 97)
            new_word.append(new_letter)
        else:
            new_word.append(i)
    return "".join(new_word)
