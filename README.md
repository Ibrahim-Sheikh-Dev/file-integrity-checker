# File Integrity Checker

A Python-based file integrity checker that uses SHA-256 cryptographic hashing to detect unauthorized file modifications.

## Features

- SHA-256 file hashing
- Baseline hash registration
- File integrity verification
- Graphical interface using Tkinter
- Modification detection
- Automated tests

## How It Works

1. Select a file.
2. Generate its SHA-256 hash.
3. Register the hash as the baseline.
4. Verify the file later.
5. The current hash is compared with the stored baseline.
6. A mismatch indicates that the file has been modified.

## Technologies

- Python
- SHA-256
- Tkinter
- JSON
- Pytest

## Project Structure

```text
file-integrity-checker/
├── src/
│   ├── main.py
│   └── integrity.py
├── tests/
│   └── test_integrity.py
├── data/
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE