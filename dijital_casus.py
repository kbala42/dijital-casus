import string

# 1. Alfabeyi Tanımla (İngilizce karakterler üzerinden matematik daha temiz çalışır)
alfabe = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
print(f"🔤 Kullanılan Alfabe: {alfabe}")

def sezar_sifrele(mesaj, kaydirma_miktari):
    """
    Bir mesajı alır ve belirtilen miktar kadar harfleri kaydırır.
    """
    sifreli_mesaj = ""
    
    # Mesajdaki her harfi tek tek incele
    for karakter in mesaj.lower():
        if karakter in alfabe:
            # 1. Harfin sırasını bul (Örn: 'a' -> 0, 'c' -> 2)
            eski_indeks = alfabe.index(karakter)
            
            # 2. Matematiksel Kaydırma (Modüler Aritmetik)
            # % len(alfabe) sayesinde 'z'den sonra başa döner
            yeni_indeks = (eski_indeks + kaydirma_miktari) % len(alfabe)
            
            # 3. Yeni harfi bul ve ekle
            yeni_karakter = alfabe[yeni_indeks]
            sifreli_mesaj += yeni_karakter
        else:
            # Harf değilse (boşluk, nokta, ünlem) olduğu gibi bırak
            sifreli_mesaj += karakter
            
    return sifreli_mesaj

def sezar_coz(sifreli_mesaj, kaydirma_miktari):
    """
    Şifreli mesajı geri çözer (Tersine işlem)
    """
    # Şifrelerken ileri (+) gittiysek, çözerken geri (-) gideriz
    # Matematikte negatif modül işlemi de Python'da düzgün çalışır
    return sezar_sifrele(sifreli_mesaj, -kaydirma_miktari)

# --- ANA PROGRAM ---

print("\n🕵️  DİJİTAL CASUS: Şifreleme Aracı Başlatıldı...")

# Kullanıcıdan veri al
gizli_mesaj = input("Lütfen şifrelenecek mesajı girin (Örn: hello world): ")
anahtar = int(input("Kaç harf kaydırılsın? (Anahtar Sayı): "))

# 1. Şifreleme
sifreli_hal = sezar_sifrele(gizli_mesaj, anahtar)
print(f"\n🔒 ŞİFRELENMİŞ MESAJ: {sifreli_hal}")
print("-" * 30)

# 2. Doğrulama (Geri Çözme)
print("🔓 Çözme testi yapılıyor...")
cozulmus_hal = sezar_coz(sifreli_hal, anahtar)
print(f"✅ ORİJİNAL MESAJ: {cozulmus_hal}")
