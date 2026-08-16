import tempfile
from pathlib import Path

from src.integrity import calculate_sha256


def test_sha256_changes_when_file_changes():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "test.txt"

        file_path.write_text("Original content")
        original_hash = calculate_sha256(str(file_path))

        file_path.write_text("Modified content")
        modified_hash = calculate_sha256(str(file_path))

        assert original_hash != modified_hash


def test_same_file_produces_same_hash():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "test.txt"

        file_path.write_text("Hello World")

        hash_one = calculate_sha256(str(file_path))
        hash_two = calculate_sha256(str(file_path))

        assert hash_one == hash_two