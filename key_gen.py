from collections.abc import Iterator
from config import Config


def generate_all_keys(key_size: int) -> Iterator[str]:
    """
    Generator of all possible key combinations using the given key size and ALLOWED_KEY_CHARS.
    """

    base = len(Config.ALLOWED_KEY_CHARS)
    index_list = [0] * key_size

    while True:
        key = "".join(Config.ALLOWED_KEY_CHARS[i] for i in index_list)
        yield key

        pos = key_size - 1
        while pos >= 0:
            if index_list[pos] < base - 1:
                index_list[pos] += 1
                break
            else:
                index_list[pos] = 0
                pos -= 1
        else:
            break
