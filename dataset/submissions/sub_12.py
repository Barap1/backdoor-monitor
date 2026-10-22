def is_palindrome(s):
    chars = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True
