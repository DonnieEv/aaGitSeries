import string

plaintext = input("What is the expression? ")
shift = int(input("How far to shift? "))

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    upper = string.ascii_uppercase
    shifted_upper = upper[shift:] + upper[:shift]

    table = str.maketrans(alphabet + upper, shifted_alphabet + shifted_upper)
    return plaintext.translate(table)

print(caesar(plaintext, shift))