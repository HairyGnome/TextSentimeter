import pytest
from Tokenizer import Tokenizer


def testTokenizer():
    tokenizer = Tokenizer()
    assert tokenizer.tokenize('Hello') == [72, 101, 108, 108, 111]
    assert tokenizer.tokenize('Gaius Octavianus Germanicus Augustus') == [71, 97, 105, 1, 79, 99, 116, 97, 118, 105, 2, 1, 71, 101, 114, 109, 2, 105, 99, 1, 65, 117, 103, 0, 116, 0]