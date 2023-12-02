import streamlit as st
import hashlib

def generate_key(seed, length):
    key = hashlib.sha256(seed.encode()).digest()[:length]
    return key

def encrypt_decrypt(message, key, is_encrypt=True):
    result = bytearray()
    for i in range(len(message)):
        if is_encrypt:
            result.append(message[i] ^ key[i % len(key)])
        else:
            result.append(message[i] ^ key[i % len(key)])
    return bytes(result)

def main():
    message_input = st.text_input("Masukkan pesan:")
    seed_input = st.text_input("Masukkan seed untuk kunci:")
    status = st.radio("Pilih Aksi:", ["Enkripsi", "Dekripsi"])

   
    if st.button("Proses"):
        key_length = len(message_input)
        key = generate_key(seed_input, key_length)

        # Proses enkripsi
        encrypted_message = encrypt_decrypt(message.encode(), key)
        st.write("Pesan terenkripsi:", encrypted_message)

        # Proses dekripsi
        decrypted_message = encrypt_decrypt(encrypted_message, key)
        st.write("Pesan terdekripsi:", decrypted_message.decode())

if __name__ == "__main__":
    main()
