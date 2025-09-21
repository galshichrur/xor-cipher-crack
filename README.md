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
python main.py examples/test.txt 3 --int-list -t 5
```

```bash
Welcome to XOR Cipher Crack!
Cipher text file: output.txt is read.
Ciphertext ASCII int list:      [32, 13, 22, 84, 58, 4, 7, 29, 27, 11, 18, 24, 84, 54, 22]...
Starting scoring guesses...
Scoring guesses...  [####################################]  100%          
Starting sorting scored guesses...
Successfully sorted guesses!
Top 30 guesses:
Guess #1        Score: 0.9684546032795074        Key: test       Plaintext: The National Security Agency (NSA) is an intellige...
Guess #2        Score: 0.96655377070421          Key: uest       Plaintext: Uhe Oatinnal!Sectritx Agdncy!(NS@) ir an!intdllife...
Guess #3        Score: 0.9663014878821152        Key: tdst       Plaintext: Tie N`tiooal Recusity!Ageocy )NSA( is!an hntemligd...
Guess #4        Score: 0.9619474465900433        Key: tert       Plaintext: Thd Nauion`l Sdcurhty @genby (OSA)!is `n iotelmige...
Guess #5        Score: 0.9569772074978466        Key: tesu       Plaintext: The!Nathonam Seburiuy Afencx (NRA) hs ao inuellhge...
```


## Notes

LLM scorer is optional. If you don't have Ollama, the tool still works with the built in scorers.

If you use a CPU machine, prefer small models or skip LLM step for speed.