#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_sentence = tuple(sentence)
    if len(sentence) == 0:
        return (0, None)
    tuple_a = (len(sentence), tuple_sentence[0])
    return tuple_a
