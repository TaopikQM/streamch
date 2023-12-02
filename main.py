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

    if st.button("Enkripsi"):
        key_length = len(message_input)
        key = generate_key(seed_input, key_length)

        encrypted_message = encrypt_decrypt(message_input.encode(), key)
        st.write("Pesan terenkripsi:", encrypted_message)

    if st.button("Dekripsi"):
        decrypted_message_placeholder = st.empty()

        if 'encrypted_message' not in locals():
            st.error("Anda perlu mengenkripsi pesan terlebih dahulu sebelum dapat mendekripsinya.")
        else:
            decrypted_message = encrypt_decrypt(encrypted_message, key)
            decrypted_message_placeholder.write("Pesan terdekripsi:", decrypted_message.decode())

if __name__ == "__main__":
    main()
