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
    st.title("Aplikasi Enkripsi & Dekripsi")

    # Input pesan yang akan dienkripsi
    message = st.text_input("Masukkan pesan:")

    # Input kunci (gunakan seed untuk menghasilkan kunci yang sama setiap kali program dijalankan)
    seed = st.text_input("Masukkan seed untuk kunci:")

    if st.button("Enkripsi / Dekripsi"):
        key_length = len(message)
        key = generate_key(seed, key_length)

        # Proses enkripsi atau dekripsi
        result = encrypt_decrypt(message.encode(), key)

        if isinstance(result, str):
            st.write("Pesan terdekripsi:", result)
        else:
            try:
                st.write("Pesan terenkripsi:", result.decode())
            except UnicodeDecodeError:
                st.error("Gagal mendekripsi pesan. Pastikan pesan yang Anda masukkan benar.")

if __name__ == "__main__":
    main()
