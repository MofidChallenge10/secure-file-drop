"""Small authenticated file encryption utility (requires cryptography)."""
from pathlib import Path
import argparse, os
from cryptography.fernet import Fernet, InvalidToken

def generate_key(path: Path) -> None:
    path.write_bytes(Fernet.generate_key())
    try: os.chmod(path, 0o600)
    except OSError: pass

def transform(source: Path, destination: Path, key_path: Path, decrypt=False) -> None:
    cipher = Fernet(key_path.read_bytes().strip())
    data = source.read_bytes()
    try: output = cipher.decrypt(data) if decrypt else cipher.encrypt(data)
    except InvalidToken as exc: raise ValueError("Invalid key or corrupted ciphertext") from exc
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(output)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest="cmd",required=True)
    k=sub.add_parser("key"); k.add_argument("path",type=Path)
    for name in ("encrypt","decrypt"):
        q=sub.add_parser(name); q.add_argument("source",type=Path); q.add_argument("destination",type=Path); q.add_argument("--key",required=True,type=Path)
    a=p.parse_args()
    if a.cmd=="key": generate_key(a.path)
    else: transform(a.source,a.destination,a.key,a.cmd=="decrypt")
if __name__=="__main__": main()
