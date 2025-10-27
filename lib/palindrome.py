import re


def longest_palindromic_substring(s):
    """
    Given a string s (1 <= len(s) <= 1000, only English letters and digits),
    return the longest palindromic substring.
    """
    # Input validation
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    if not (1 <= len(s) <= 1000):
        raise ValueError("Length of s must be between 1 and 1000.")
    if not re.fullmatch(r"[A-Za-z0-9]+", s):
        raise ValueError("String must contain only English letters and digits.")

    n = len(s)
    if n < 2:
        return s

    start = 0
    max_len = 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_curr_len = max(len1, len2)
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2

    return s[start : start + max_len]
