def is_anagram(a, b):
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())
