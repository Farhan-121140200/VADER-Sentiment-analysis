from deep_translator import GoogleTranslator

def terjemahkan_teks(teks):
    """
    Menerjemahkan teks dari bahasa Indonesia ke bahasa Inggris.

    Parameter:
    - teks (str): Teks dalam bahasa Indonesia.

    Return:
    - str: Teks yang sudah diterjemahkan ke bahasa Inggris.
    """
    try:
        return GoogleTranslator(source="id", target="en").translate(teks)
    except Exception as e:
        print(f"Terjadi kesalahan saat menerjemahkan: {e}")
        return teks  # Kembalikan teks asli jika gagal
