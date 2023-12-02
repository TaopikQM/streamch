import streamlit as st
import hashlib

def generate_key(seed, length):
    key = hashlib.sha256(seed.encode()).digest()[:length]
    return key

def encrypt_decrypt(message, key):
    encrypted = bytearray()
    for i in range(len(message)):
        encrypted.append(message[i] ^ key[i % len(key)])
    return bytes(encrypted)

def main():
    # Input pesan yang akan dienkripsi
    message = st.text_input("Masukkan pesan:")
    
    # Input kunci (gunakan seed untuk menghasilkan kunci yang sama setiap kali program dijalankan)
    seed = st.text_input("Masukkan seed untuk kunci:")
    
    if st.button("Enkripsi"):
        key_length = len(message)
        key = generate_key(seed, key_length)

        # Proses enkripsi
        encrypted_message = encrypt_decrypt(message.encode(), key)
        st.write("Pesan terenkripsi:", encrypted_message)

    if st.button("Dekripsi"):
        decrypted_message = encrypt_decrypt(encrypted_message, key)
        st.write("Pesan terdekripsi:", decrypted_message.decode())

if __name__ == "__main__":
    main()
