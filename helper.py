import string
from config import Config


def english_score(text: str) -> float:
    """
    Return chi-square score for how close text is to English letter frequencies.
    """

    text = text.upper()
    letters = [c for c in text if c in string.ascii_uppercase]
    if not letters:
        return 0.0

    n = len(text)
    if n == 0:
        return 0.0

    counts = {}

    for c in string.ascii_uppercase:
        counts[c] = letters.count(c)

    chi_sq = 0.0
    for char, freq in Config.ENGLISH_FREQ.items():
        current = counts.get(char, 0)
        expected = n * (freq / 100)
        if expected > 0:
            chi_sq += (current - expected) ** 2 / expected

    return 1.0 / (1.0 + chi_sq / n)

def printable_chars_ratio(text: str) -> float:
    """
    Calculates the ratio of printable characters in text.
    """

    printable_chars_count = 0
    for char in text:
        if 32 <= ord(char) <= 126:
            printable_chars_count += 1
    return printable_chars_count / len(text)
