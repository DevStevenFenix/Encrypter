from cryptography.fernet import Fernet

def generateKey(keyFileLoc):
    key = Fernet.generate_key()
    with open(keyFileLoc, 'wb') as filekey:
        filekey.write(key)
        
def Encrypt(filekeyloc, location, encryptedLocation): 
    with open(filekeyloc, 'rb') as filekey:
        key = filekey.read()
    
    fernet = Fernet(key)
    
    with open(location, 'rb') as file:
        original = file.read()
        
    encrypted = fernet.encrypt(original)
    
    with open(encryptedLocation, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def Decrypt(filekeyloc, location, decryptedLocation):
    with open(filekeyloc, 'rb') as filekey:
        key = filekey.read()
        
    fernet = Fernet(key)
    with open (location, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    with open(decryptedLocation, 'wb') as dec_file:
        dec_file.write(decrypted)