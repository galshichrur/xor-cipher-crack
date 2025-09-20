import ollama
from config import Config


def sort_guesses_by_llm(guesses: list[tuple[float, str, str]], model: str) -> list[tuple[float, str, str]]:

    scored_guesses = []
    for _, key, decrypted_text in guesses:
        try:
            response = ollama.chat(
                model=model,
                messages=[
                {"role": "system",
                 "content": Config.PROMPT},
                {"role": "user", "content": decrypted_text},
                ],
                options={
                    "temperature": 0,
                    "num_predict": 5,
                    "stop": ["\n"]
                }

            )
            print("*")
            scored_guesses.append((float(response["message"]["content"]), key, decrypted_text))
        except Exception as e:
            print(e)
            continue

    scored_guesses.sort(key=lambda guess: guess[0], reverse=True)  # Sort by LLM score.
    return scored_guesses
