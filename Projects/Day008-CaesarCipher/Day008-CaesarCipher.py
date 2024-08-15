print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def encrypt(message: str, shift: int) -> str:
    """

    :param message: string to be encrypted
    :param shift: number of positions each letter in message needs to be shifted
                  by
    :return: encrypted string
    """
    # upper ascii = [65, 90]
    # lower ascii = [97, 122]

    encrypted_msg = ""

    for letter in message:
        if letter == " ":
            encrypted_msg += " "
            continue

        ascii_letter = ord(letter)
        shift_ascii = ascii_letter + shift

        if (letter.isupper() and shift_ascii > 90):
            shift_ascii = shift_ascii - 26

        if (letter.islower() and shift_ascii > 122):
            shift_ascii = shift_ascii - 26

        encrypted_msg += chr(shift_ascii)

    return encrypted_msg


def decrypt(message: str, shift: int) -> str:
    """

    :param message: string to be decrypted
    :param shift: number of positions each letter in message was shifted by
    :return: decrypted string
    """
    # upper ascii = [65, 90]
    # lower ascii = [97, 122]

    decrypted_msg = ""

    for letter in message:
        if letter == " ":
            decrypted_msg += " "
            continue

        ascii_letter = ord(letter)
        shift_ascii = ascii_letter - shift

        if (letter.isupper() and shift_ascii < 65):
            shift_ascii = shift_ascii + 26

        if (letter.islower() and shift_ascii < 97):
            shift_ascii = shift_ascii + 26

        decrypted_msg += chr(shift_ascii)

    return decrypted_msg


def caesar_cipher(action: str, message: str, shift: int) -> str:
    """

    :param action: whether user wants to encrypt or decrypt
    :param message: message to be encrypted or decrypted
    :param shift: number of positions each letter in message is shifted by
    :return: encrypted or decrypted message
    """
    msg = ""
    if action == 'encode':
        msg = encrypt(message, shift)

    if action == 'decode':
        msg = decrypt(message, shift)

    return msg


again = "yes"
while again == "yes":
    user_action = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while user_action not in ['encode', 'decode']:
        user_action = input('Invalid command. Please try again.')

    user_message = input("Type your message: ")

    user_shift = int(input("Type the shift number: "))

    print(
        f'Your {user_action}d message is: {caesar_cipher(user_action, user_message, user_shift)}')
    again = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
