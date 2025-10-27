import pytest
from lib.palindrome import longest_palindromic_substring


def test_single_character():
    """When the input is a single character, the result should be that character."""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("Z") == "Z"
    assert longest_palindromic_substring("7") == "7"


def test_entire_string_is_palindrome():
    """When the entire string is a palindrome, it should return the full string."""
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("abba") == "abba"
    assert longest_palindromic_substring("A1B1A") == "A1B1A"


def test_substring_palindrome_in_middle():
    """When a palindrome appears in the middle of the string."""
    assert longest_palindromic_substring("abcba123") == "abcba"
    assert longest_palindromic_substring("123abccba456") == "abccba"


def test_multiple_palindromes_choose_longest():
    """If multiple palindromes exist, return the longest one."""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"


def test_no_repeated_characters():
    """When no repeated characters, return any single character."""
    s = "abcdefg"
    result = longest_palindromic_substring(s)
    assert len(result) == 1
    assert result in s


def test_numeric_palindrome():
    """Palindromic substrings with digits only."""
    assert longest_palindromic_substring("123454321") == "123454321"
    assert longest_palindromic_substring("12213321") == "1221"


def test_mixed_alphanumeric():
    """Palindromes with letters and digits mixed."""
    assert longest_palindromic_substring("a1b22b1a") == "a1b22b1a"
    assert longest_palindromic_substring("abc123321xyz") == "123321"


def test_case_sensitivity():
    """Ensure the function treats uppercase and lowercase as distinct unless specified otherwise."""
    assert longest_palindromic_substring("Aa") in ["A", "a"]
    assert longest_palindromic_substring("Madam") == "ada"  # 'M' != 'm'


def test_minimum_and_maximum_length_bounds():
    """Validate bounds: min length = 1, max length = 1000."""
    assert longest_palindromic_substring("x") == "x"

    long_input = "a" * 1000
    assert longest_palindromic_substring(long_input) == long_input


def test_invalid_characters_ignored():
    """Optional: ensure algorithm handles constraint violations gracefully."""
    with pytest.raises(ValueError):
        longest_palindromic_substring("abc!@#")
