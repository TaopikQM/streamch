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
    message_input = st.text_input("Masukkan pesan:")
    seed_input = st.text_input("Masukkan seed untuk kunci:")

    button("Enkripsi"):
        key_length = len(message_input)
        key = generate_key(seed_input, key_length)

        encrypted_message = encrypt_decrypt(message_input.encode(), key)
        st.write("Pesan terenkripsi:", encrypted_message)

    button("Dekripsi"):
       # Proses dekripsi
    decrypted_message = encrypt_decrypt(encrypted_message, key)
    print("Pesan terdekripsi:", decrypted_message.decode())

if __name__ == "__main__":
    main()
