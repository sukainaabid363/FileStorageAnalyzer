
import unittest
import tempfile
from pathlib import Path


class StorageAnalyzerTests(unittest.TestCase):

    def test_file_count_and_total_storage(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)

            (folder / "notes.txt").write_bytes(b"12345")
            (folder / "photo.jpg").write_bytes(b"1234567890")

            files = [
                file for file in folder.rglob("*")
                if file.is_file()
            ]

            total_size = sum(
                file.stat().st_size for file in files
            )

            self.assertEqual(len(files), 2)
            self.assertEqual(total_size, 15)


if __name__ == "__main__":
    unittest.main()
