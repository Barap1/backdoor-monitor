def run_length_encode(s):
    runs = []
    for ch in s:
        if runs and runs[-1][0] == ch and runs[-1][1] < 255:
            runs[-1] = (ch, runs[-1][1] + 1)
        else:
            runs.append((ch, 1))
    return runs
