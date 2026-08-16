import hashlib
import json
from pathlib import Path


HASH_FILE = Path("data/hashes.json")


def calculate_sha256(file_path: str) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with Path(file_path).open("rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_hash(file_path: str) -> str:
    """Calculate and save the baseline hash for a file."""
    file_hash = calculate_sha256(file_path)

    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    hashes = {}

    if HASH_FILE.exists():
        with HASH_FILE.open("r", encoding="utf-8") as file:
            hashes = json.load(file)

    hashes[str(Path(file_path))] = file_hash

    with HASH_FILE.open("w", encoding="utf-8") as file:
        json.dump(hashes, file, indent=4)

    return file_hash


def verify_integrity(file_path: str):
    """Compare current file hash against the stored baseline."""
    path = str(Path(file_path))

    if not HASH_FILE.exists():
        return None, "No baseline hash found."

    with HASH_FILE.open("r", encoding="utf-8") as file:
        hashes = json.load(file)

    if path not in hashes:
        return None, "File has not been registered."

    current_hash = calculate_sha256(file_path)
    original_hash = hashes[path]

    return current_hash == original_hash, current_hash