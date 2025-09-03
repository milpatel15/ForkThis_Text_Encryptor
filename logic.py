from cryptography.fernet import Fernet, InvalidToken

def generate_key_str() :
    return(Fernet.generate_key().decode())

def encrypt_message(message: str, key: str) -> str :
    try:
        f = Fernet(key.encode())
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()
    except (ValueError, TypeError):
        return "ERROR: Invalid Key for Encryption."
    
def decrypt_message(encrypted_message: str, key: str) -> str:
    
    try:
        f = Fernet(key.encode())
        decrypted_message = f.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
    except (InvalidToken, TypeError, ValueError):
        return "ERROR: Decryption Failed. Invalid Key or Message."