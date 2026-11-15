# Secure File Drop
A minimal local file encryption/decryption CLI using Fernet authenticated encryption.

## Install
```bash
python -m pip install -r requirements.txt
```

## Usage
```bash
python vault.py key vault.key
python vault.py encrypt private.pdf private.pdf.enc --key vault.key
python vault.py decrypt private.pdf.enc restored.pdf --key vault.key
python -m unittest discover -s tests -v
```

Keep the key separate from encrypted files and backups. Anyone holding the key can decrypt the data. This is a local utility, not a hosted upload service.
