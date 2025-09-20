
class Config:
    PROMPT = """
Rate how likely the following text is valid, natural plain English on a scale from 0.00 to 1.00.
Return ONLY a single decimal number between 0 and 1 (For example: 0.73).
**DON'T ADD ANY EXTRA TEXT OR EXPLANATION!**
"""

    ALLOWED_KEY_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ENGLISH_FREQ = {
        'E': 12.0, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7,
        'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8,
        'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0,
        'P': 1.9, 'B': 1.5, 'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
        'Q': 0.1, 'Z': 0.07
    }

    PRINTABLE_WEIGHT = 0.6
    ENGLISH_WEIGHT = 0.4
