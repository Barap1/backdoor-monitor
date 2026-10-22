def is_anagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    if len(a) != len(b):
        return False
    if a == b:
        return True
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True
