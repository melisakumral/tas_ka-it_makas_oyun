import random
import time
import os

def bilgisayar_secimi_yap():
    seçenekler = ["taş", "kağit", "makas"]
    return random.choice(seçenekler)

#kullanici=input("taş kağit makas arasindan birini seçiniz: ")

def kazanan_belirle(kullanici,bilgisayar):
 if kullanici==bilgisayar:
   return "berabere"
 elif (kullanici=="taş" and bilgisayar=="makas")or\
      (kullanici=="makas" and bilgisayar=="kağit")or\
      (kullanici=="kağit" and bilgisayar=="taş"): 
      return "kullanici"

 else :
    return "bilgisayar"
 

def tur_sonucu(kullanici_seçimi,bilgisayar_seçimi,tur_kazanani):
   print(f"kullanıcı seçimi:{kullanici_seçimi}  -  bilgisayar seçimi:{bilgisayar_seçimi}")
   if tur_kazanani == "berabere":
        print("Tur sonucu: Berabere!")
   else:
        print(f"Tur sonucu: {tur_kazanani} kazandı!")


def oyunu_tekrar_oynama(kullanici_cevabi,bilgisayarin_cevabi):
    kullanici_cevabi= input("tekrar oynamak ister misiniz\2 (evet/hayır) :")
    bilgisayarin_cevabi = random.choice(["evet","hayır"])
    print(f"bilgisayarın tekrar oynama cevabı :{bilgisayarin_cevabi}")
    return kullanici_cevabi == "evet" and bilgisayar_cevabi == "evet"

def kazanan_efekti(kazanan):
    konfeti = ['*', '.', 'o', 'x', '+','-','/']
    
    for _ in range(10):  # 10 kez yanıp sönsün
        os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle
        print("\n" * 4)  # Ekranın ortasına yazmak için birkaç satır boşluk ekle
        
        # Konfeti efektini simüle etmek için rastgele yerleştir
        for _ in range(20):
            print(" " * random.randint(0, 50) + random.choice(konfeti))
        
        print(" " * 30 + kazanan.upper(), end="\r")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı tekrar temizle
        time.sleep(0.5)

    print(f"{kazanan} kazandı!")  # Son olarak kazananı yazdır

def tas_kağit_makas_MELİSA_KUMRAL():
    print("Taş, Kağit, Makas Oyununa Hoş Geldiniz!")
    print("Her oyuncu taş, kağit, makas arasından bir seçim yapar")
    print("Taş makası yener.\nMakas kağidi yener.\nKağit taşı yener.")
    while True:
        kullanici_puan = 0
        bilgisayar_puan = 0
        round_sayisi = 1
        while kullanici_puan < 2 and bilgisayar_puan < 2:
            print(f"\nRound {round_sayisi}")
            kullanici_secimi = input("Taş, kağit, makas arasından birini seçin: ").lower()
            bilgisayar_secimi = bilgisayar_secimi_yap()
            kazanan = kazanan_belirle(kullanici_secimi, bilgisayar_secimi)
            tur_sonucu(kullanici_secimi, bilgisayar_secimi, kazanan)
            
            if kazanan == "kullanici":
                kullanici_puan += 1
            elif kazanan == "bilgisayar":
                bilgisayar_puan += 1
            
            round_sayisi += 1
        if kullanici_puan == 2:
            print("\nOyunu Kazandınız!")
            kazanan_efekti("Kullanıcı")
        else:
            print("\nBilgisayar Oyunu Kazandı!")
            kazanan_efekti("Bilgisayar")
        
        if not tekrar_oynamak_ister_misin():
            print("Oyun Bitti. Tekrar görüşmek üzere!")
            break

# Oyunu başlat
tas_kağit_makas_MELİSA_KUMRAL()
