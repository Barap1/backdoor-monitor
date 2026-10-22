def flatten(nested):
    result = []
    stack = [iter(nested)]
    while stack:
        for item in stack[-1]:
            if isinstance(item, list):
                stack.append(iter(item))
                break
            result.append(item)
        else:
            stack.pop()
    return result
