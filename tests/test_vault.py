import tempfile, unittest
from pathlib import Path
from vault import generate_key, transform
class VaultTests(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/"plain").write_bytes(b"private data"); generate_key(root/"key")
            transform(root/"plain",root/"cipher",root/"key"); transform(root/"cipher",root/"restored",root/"key",True)
            self.assertEqual((root/"restored").read_bytes(),b"private data")
    def test_wrong_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); generate_key(root/"k1"); generate_key(root/"k2"); (root/"c").write_bytes(b"bad")
            with self.assertRaises(ValueError): transform(root/"c",root/"out",root/"k1",True)
if __name__=="__main__": unittest.main()
