import os

import pytest
from Tokenizer import Tokenizer
from DatabaseParser import DatabaseParser


def test_tokenizer():
    tokenizer = Tokenizer()
    assert tokenizer.tokenize('Hello') == [72, 101, 108, 108, 111]
    assert tokenizer.tokenize('Gaius Julius') == [71, 97, 1, 32, 74, 117, 108, 1]

def test_database_parser():
    parser = DatabaseParser(1, False)
    tokenizer = Tokenizer()
    data, labels, eval_data, eval_labels = parser.parse_data(os.curdir + '/data/dsm.csv')
    assert data[0] == tokenizer.tokenize("@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D")
    assert labels[0] == 0
    assert data[6] == tokenizer.tokenize("Need a hug")
    assert labels[6] == 0
    assert eval_data == []
    assert eval_labels == []
    assert len(data) == 21
    assert len(labels) == 21