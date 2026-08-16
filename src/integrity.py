import hashlib
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent #point to root folder
HASH_FILE = PROJECT_ROOT / "data" / "hashes.json" #reconstructing to data folder hash file


def calculate_sha256(file_path: str) -> str:
    sha256 = hashlib.sha256()

    #open file as binary data. rb =  read, binary
    with Path(file_path).open("rb") as file:
        #read the file in chunks in 8192 bytes
        while chunk := file.read(8192):
            #feeding the data into sha256
            sha256.update(chunk)
    #convert 256 bits to 64 hexadecimal character eg asdhasdh19389x28basd...
    return sha256.hexdigest()

#saving the file as baseline
def save_hash(file_path: str) -> str:
    #stores the result into file hash
    file_hash = calculate_sha256(file_path)

    #hash file is data/hashes.json
    HASH_FILE.parent.mkdir(parents=True, exist_ok=True)

    #empty dict
    hashes = {}

    if HASH_FILE.exists():
        with HASH_FILE.open("r", encoding="utf-8") as file:
            hashes = json.load(file)

    absolute_path = str(Path(file_path).resolve())
    hashes[absolute_path] = file_hash #store the hash

    with HASH_FILE.open("w", encoding="utf-8") as file:
        json.dump(hashes, file, indent=4) #effectively making { "file(path)": hash}

    return file_hash


def verify_integrity(file_path: str):
    if not HASH_FILE.exists():
        return None, "No baseline hash found."

    with HASH_FILE.open("r", encoding="utf-8") as file:
        hashes = json.load(file)

    absolute_path = str(Path(file_path).resolve())

    if absolute_path not in hashes:
        return None, "File has not been registered."

    current_hash = calculate_sha256(file_path)
    original_hash = hashes[absolute_path]

    return current_hash == original_hash, current_hash