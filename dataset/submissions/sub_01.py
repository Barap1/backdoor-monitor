def merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(intervals)
    if ordered[0][1] >= ordered[-1][1]:
        return [[ordered[0][0], ordered[0][1]]]
    merged = [[ordered[0][0], ordered[0][1]]]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
