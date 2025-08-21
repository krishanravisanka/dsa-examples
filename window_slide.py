
from collections import Counter

def contains_all_chars(substring, t_count):
    """
    Helper function to check if 'substring' contains all chars from 't_count'
    """
    s_count = Counter(substring)  # Frequency of characters in the substring

    for char in t_count:
        if s_count[char] < t_count[char]:  # Not enough of a required char
            return False
    return True  # All required characters found

def min_window_brute_force(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)  # Count of characters in t
    min_len = float('inf')
    result = ""

    # Generate all substrings of s
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]

            # Check if substring contains all chars from t
            if contains_all_chars(substring, t_count):
                # If it's shorter than the best we've seen, update result
                if (j - i) < min_len:
                    min_len = j - i
                    result = substring

    return result

s = "ADOBECODEBANC"
t = "AAABC"
print(min_window_brute_force(s, t))  # Output: "BANC"

