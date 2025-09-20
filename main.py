import click
from bruteforce import guess_keys, score_guesses
from llm_local import sort_guesses_by_llm
from xor_cipher import XORCipher


@click.command()
@click.argument("path")
@click.argument("key-size", type=int)
@click.option("--int-list", is_flag=True, help="ciphertext is int list")
@click.option("--llm", is_flag=True, help="use llm to sort top guesses")
@click.option("-m", "--model", default="phi", help="LLM model  (default: mistral)")
@click.option("-t", "--top", default=30, help="how many top guesses to sort by LLM (default: 10)")
@click.option("-s", "--sep", default=",", help="separator for int list")
def main(path: str, key_size: int, int_list: bool, llm: bool, model: str, top: int, sep: str):

    print("Welcome to XOR Cipher Crack!")

    if key_size <= 0:
        print("Key size must be greater than 0.")

    if key_size > 7:
        print("Key size must be less than 7.")

    # Read given path file content.
    with open(path, "rb") as ciphertext_file:
        ciphertext = ciphertext_file.read().decode()
        ciphertext_file.close()

    if ciphertext is None:
        print("Invalid path to ciphertext file.")
        return None
    else:
        print(f"Cipher text file: {path} is read.")

    if int_list:  # If ciphertext is ASCII list of integers.
        ct_ascii_list = [int(num) for num in ciphertext.split(sep)]

    else:  # If ciphertext is pure string.
        ct_ascii_list = XORCipher.to_ascii_list(ciphertext)

    print(f"Ciphertext ASCII int list:\t{ct_ascii_list[:15]}...")
    bruteforce_iter = guess_keys(ct_ascii_list, key_size)
    print("Starting bruteforce...")
    guesses = score_guesses(bruteforce_iter)
    print("Successfully sorted guesses!")
    print(f"Top {top} guesses:")
    for i, guess in enumerate(guesses[:top]):
        print(f"Guess #{i+1}\tScore: {guess[0]}\t Key: {guess[1]}\t Plaintext: {guess[2][:50]}...")

    if not llm:
        return None

    print(f"Sorting by {model} LLM model...")
    llm_sorted = sort_guesses_by_llm(guesses[:top], model)
    print("Successfully sorted guesses by LLM!")
    for i, guess in enumerate(llm_sorted[:top]):
        print(f"Guess #{i+1}\tLLM Score: {guess[0]}\tKey: {guess[1]}\t Plaintext: {guess[2][:50]}...")
    return None

if __name__ == '__main__':
    main()
