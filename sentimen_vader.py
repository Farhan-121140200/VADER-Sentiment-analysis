import json
import emoji
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Inisialisasi VADER
analyzer = SentimentIntensityAnalyzer()

# Fungsi memuat kamus kata tambahan dari JSON
def load_custom_lexicon(file_path="custom_lexicon.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            custom_words = json.load(file)
            analyzer.lexicon.update(custom_words)  # Tambahkan ke VADER
            print(f"✅ {len(custom_words)} kata tambahan dimuat ke dalam VADER!")
    except Exception as e:
        print(f"⚠️ Gagal memuat custom lexicon: {e}")

# Fungsi memuat kamus emoji dari JSON
def load_emoji_lexicon(file_path="emoji_sentiment.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            emoji_data = json.load(file)
             # Normalisasi format emoji menjadi string eksplisit
            positif = set(map(str, emoji_data["positif"]))
            negatif = set(map(str, emoji_data["negatif"]))
            print(f"✅ {len(positif)} emoji positif & {len(negatif)} emoji negatif dimuat!")
            return positif, negatif
    except Exception as e:
        print(f"⚠️ Gagal memuat emoji lexicon: {e}")
        return set(), set()

# Muat lexicon kata & emoji
load_custom_lexicon()
emoji_positif, emoji_negatif = load_emoji_lexicon()

# Cek apakah emoji dimuat
print("Emoji Positif:", emoji_positif)
print("Emoji Negatif:", emoji_negatif)

def analisis_sentimen(teks):
    """
    Melakukan analisis sentimen pada teks bahasa Inggris menggunakan VADER.
    Juga menganalisis sentimen emoji jika ada.

    Parameter:
    - teks (str): Teks dalam bahasa Inggris.

    Return:
    - dict: Skor sentimen dan klasifikasi (positif, negatif, netral).
    """
    # Analisis sentimen teks dengan VADER
    hasil = analyzer.polarity_scores(teks)

    # Deteksi emoji dalam teks
    sentimen_emoji = 0
    for char in teks:
        if char in emoji_positif:
            sentimen_emoji += 0.5
        elif char in emoji_negatif:
            sentimen_emoji -= 0.5

    # Debug: Lihat nilai VADER & Emoji sebelum penggabungan
    print(f"VADER Compound Score: {hasil['compound']}, Sentimen Emoji: {sentimen_emoji}")

    # Gabungkan sentimen emoji dengan hasil teks
    total_score = hasil['compound'] + sentimen_emoji
    
    if total_score >= 0.05:
        sentimen = "positif"
    elif total_score <= -0.05:
        sentimen = "negatif"
    else:
        sentimen = "netral"

    return {
        "teks": teks,
        "sentimen": sentimen,
        "skor": hasil,
        "skor_emoji": sentimen_emoji,
        "total_score": total_score
    }

