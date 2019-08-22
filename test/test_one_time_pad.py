"""
One-Time-Pad Coder

Encrypts and decrypts a text using the one-time-pad algorithm.
"""
from random import seed
from algo.one_time_pad import *


def test_genkey():
    seed(121)
    key1 = "".join(generate_key("Today is ok"))
    assert key1 == "lB-Y=w;%wQK"


def test_num():
    assert to_number_code('a') == 0


def test_mod_add():
    return modular_operation('a', 'b', len(PAD), add) == 1


def test_enc():
    seed(121)
    text = "Today is a good day to py"
    key = generate_key(text)
    assert encrypt(text, key) == "4P:Yjv][vQJDa'k\\a:<pw-16>"


def test_dec():
    text = "4P:Yjv][vQJDa'k\\a:<pw-16>"
    key = "lB-Y=w;%wQKx>2h]}:3qd82R5"
    assert decrypt(text, key) == "Today is a good day to py"
