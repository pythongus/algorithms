"""
One-Time-Pad Coder

Encrypts and decrypts a text using the one-time-pad algorithm.
"""
from random import choice
from string import ascii_letters, digits, punctuation
from itertools import chain
from operator import add, sub


PAD = list(chain(ascii_letters, digits, punctuation, [' ']))


def generate_key(text):
    return [choice(PAD) for _ in range(len(text))]


def encrypt(text, key):
    return one_time_pad(text, key, add)


def decrypt(text, key):
    return one_time_pad(text, key, sub)


def one_time_pad(text, key, operation):
    return "".join([modular_operation(ch1, ch2, len(PAD), operation) for ch1, ch2 in list(zip(text, key))])


def modular_operation(char1, char2, size, operation):
    return to_character(operation(to_number_code(char1), to_number_code(char2)) % size)


def to_number_code(char):
    return PAD.index(char)


def to_character(num):
    return PAD[num]


if __name__ == "__main__":
    text = ("""v+6aq2LWK6j=~/J,Nl$<]DsvAiM1L*6FOlwQ:=tR}y;lhI]2$#uVd\\"""
            """#JXkIF4\\(*NR8OrOaHt 3oO0;DL]\'I3^?``X\\X!QIGy6\'/892?o"""
            """1p9cgfUn#u(u@YQ> )WXq+dNIRdbt9?\\^{X0="F*u""")
    key = """<place key here>"""
    print(decrypt(text, key))
