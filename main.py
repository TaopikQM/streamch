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

        if status == "Enkripsi":
            # Proses enkripsi
            result_message = encrypt_decrypt(message_input.encode(), key, is_encrypt=True)
            st.write("Pesan terenkripsi:", result_message.hex())
        elif status == "Dekripsi":
            # Proses dekripsi
            result_message = encrypt_decrypt(bytes.fromhex(message_input), key, is_encrypt=False)
            st.write("Pesan terdekripsi:", result_message.decode())

if __name__ == "__main__":
    main()
