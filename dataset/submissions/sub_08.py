def is_valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack:
                return False
            if stack[-1] == pairs[ch]:
                stack.pop()
    return not stack
