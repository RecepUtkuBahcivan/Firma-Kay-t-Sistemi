#Fonksiyon, Class, Döngüler, Karar, Dosyalama, Liste-Demet, Sözlük,Veritabanı
#ONLİNE YEMEK SEKTÖRÜNDE FİRMA KAYIT SİSTEMİ

import sqlite3
con = sqlite3.connect("bilgiler.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (Ad TEXT, Tür TEXT, Sahip TEXT, Lokasyon TEXT, Müşteri INT )")
    con.commit()
tablo_olustur()
def veri_ekle(firma_adı,firma_türü,firma_sahibi,firma_lokasyonu,müsteri_sayisi):
    cursor.execute("Insert into bilgiler VALUES (?,?,?,?,?)", (firma_adı,firma_türü,firma_sahibi,firma_lokasyonu,müsteri_sayisi))
    con.commit()


personel=[]
class Personel:
    def personeladı(self):
        ad=input("Personel Adı:")
        personel.append(ad)
    def personelsoyad(self):
        soyad=input("Personel Soyadı:")
        personel.append(soyad)
    def personelyaşı(self):
        yaş=int(input("Personel Yaşı:"))
        personel.append(yaş)

def ortalama():
    ortalamam = ort/sayac
    print("Girilen Firmaların Ortalama Müşteri Sayısı {}.".format(ortalamam))
    return ortalamam

print("Personel Giriş Ekranına Hoş geldiniz!")
a=Personel()
a.personeladı()
a.personelsoyad()
a.personelyaşı()
print(personel)
print("Firma Kayıt Sistemine Gidiliyor....\n")


print("****Firma Kayıt Sistemine Hoş geldiniz****\n")
sayac = int(input("Sisteme Girilecek Şirket Sayısını Giriniz:"))
while True:

    ort=0
    firmalar = []
    for i in range(1,sayac+1):
        bilgiler = []
        firmablg = {"Girilen Firmanın Bilgisi : ":bilgiler}
        firma_adı = input("Firma Adını Giriniz: ")
        bilgiler.append(firma_adı)
        firma_türü = input("Firma Türünü Giriniz(Tatlı, Kebap, Fastfood):")
        bilgiler.append(firma_türü)
        firma_sahibi = input("Firma Sahibi İsmini Giriniz:")
        bilgiler.append(firma_sahibi)
        firma_lokasyonu = input("Firma Lokasyonunu Giriniz:")
        bilgiler.append(firma_lokasyonu)
        müsteri_sayisi = int(input("Ortalama Müşteri Sayınızı Giriniz:"))
        ort += müsteri_sayisi
        bilgiler.append(müsteri_sayisi)
        veri_ekle(firma_adı, firma_türü, firma_sahibi, firma_lokasyonu, müsteri_sayisi)
        con.close()
        if firma_adı.count("A", 0, 1):
            print("Firma adınız A harfi ile başlamakta.")
            firmalar.append(firma_adı)
        else:
            print("Firma Adınız A harfi ile başlamamakta.")
        sonuc = print(firmablg)
        çıkış = int(input("Kayıta devam etmek için 1'e, çıkış yapmak için 2'ye basınız!"))
        if çıkış == 1:
            continue
        elif çıkış == 2:
            print("A Harfi ile Başlayan Firmalar {}".format(firmalar))
            ortalama()
            file = open("firmabilgileri.txt", "w", encoding="utf-8")
            file.write(str(personel))
            file.write("\n")
            file.write(str(bilgiler))
            file.close()
            exit()


