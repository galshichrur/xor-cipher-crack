# XOR Cipher Crack

Breaking repeated key XOR cipher with brute force and scoring.

This project started from a Project Euler challenge.
I expanded it to learn more about XOR, OTP, and simple cryptanalysis after reading Serious Cryptography.

---

## Features
- Bruteforce search over repeated key XOR ciphers
- Scoring by printable character ratio + English frequency analysis
- Optional reranking with a local LLM (using Ollama)
- Examples ciphertexts included (`examples/` folder)

---

## Installation

- Python 3.8+ recommended.

- Create a virtual environment
```bash
python -m venv .venv
# mac / linux
source .venv/bin/activate
# windows (PowerShell)
.venv\Scripts\Activate.ps1
```
- Install Python deps
```bash
pip install -r requirements.txt
```
- Install Ollama and pull a fast local model
```bash
ollama pull mistral
```

## Usage

```bash
python main.py <path> <key_size> [--int-list] [--llm] -m <model> -t <top> -s <sep>
```

## Example run
```bash
python main.py examples/gal.txt 3 --int-list -t 5
```

```bash
Welcome to XOR Cipher Crack!
Cipher text file: examples/gal.txt is read.
Ciphertext ASCII int list:      [51, 9, 9, 71, 0, 14, 8, 23, 9, 71, 6, 30, 8, 20, 28]...
Starting bruteforce...
Successfully sorted guesses!
Top 5 guesses:
Guess #1        Score: 0.5999420190408604        Key: cal        Plaintext: Phe$abkve$grkupw cen fe `esgrifed$alcebvaigalhy es...
Guess #2        Score: 0.5999139004353743        Key: gal        Plaintext: The above groups can be described algebraically as...
Guess #3        Score: 0.5998306816009502        Key: gtl        Plaintext: T}e tboce rro`ps5ca{ bp dpscgibpd tlgpbrtictlll af...
Guess #4        Score: 0.5997353149086031        Key: gah        Plaintext: Tha afova gvouts gan$be$dewcrmbe` ahgeframcahly$as...
Guess #5        Score: 0.5997176313325514        Key: fal        Plaintext: Uhe!abnve!grnupr c`n ce eesbriced!alfebsaibalmy `s...
```


## Notes

LLM scorer is optional. If you don't have Ollama, the tool still works with the built in scorers.

If you use a CPU machine, prefer small models or skip LLM step for speed.