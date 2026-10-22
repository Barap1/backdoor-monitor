from itertools import groupby


def run_length_encode(s):
    return [(ch, len(list(group))) for ch, group in groupby(s)]
