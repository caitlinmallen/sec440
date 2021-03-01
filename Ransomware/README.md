# SEC 440
## Ransomware Proof of Concept

This is a proof of concept malware that is not to be used for malicious purposes
This is ransomware has depencies of Python3 and the cryptography library. It assumes the test target has these.
 

## Dependecies
* Cryptography

## How it works

A target directory can be set inside the ransom.py file. The program will first download a public key and save it to the victims machine. It then generates a symmetric key using the fernet library from _Cryptography_. This key is then encrypted using the public key and writen to the victim machine. The unencrypted symmetric key in memory is then used to encrypt the files in the target directory and overwrite them. The program then ends.

To decrypt the files, the private key is needed. The decrypt program first accepts the encrypted symmetric key, which has to be passed on the command line. The encrypted key is then decrypted using the private key. The symmetric key is then held in memory and then used to decrypt the target folders, writing out the decrypted content


## References used:
* https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_symmetric_and_asymmetric_cryptography.htm
* https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
