from collections.abc import Iterator

ALLOWED_KEY_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_all_keys(key_size: int) -> Iterator[str]:
    """
    Generator of all possible key combinations using the given key size and ALLOWED_KEY_CHARS.
    """

    base = len(ALLOWED_KEY_CHARS)
    index_list = [0] * key_size

    while True:
        key = "".join(ALLOWED_KEY_CHARS[i] for i in index_list)
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
