import time
import random
import webbrowser

#Versiyon, ve başlangıçtaki değişken bilgileri yazar
versiyon = "0.4"
anaMenuCevap = None

#Ana Menü kodları buradadır
print("""
DexTool'a hoşgeldiniz.
Bu yazılım geliştirme aşamasındadır ve yenilikler eklenmeye devam edecektir.
Versiyon:""", versiyon)

#MENU DEF
def menu0():
  print("== ANA MENÜ ==\n")
  print("Yapabileceklerin aşağıda listelenmiştir.")
  print("[1] Oyun Oyna\n[2] Bağlantılar\n[3] Çıkış Yap\n")
  menu0 = input("Cevabınızı bekliyorum.\n")
  if menu0 == "1":
    menu01()
  elif menu0 == "2":
    menu02()
  elif menu0 == "3":
    print("Program kendini 3 saniye içerisinde kapatacaktır.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Görüşmek üzere.")
    time.sleep(1)
    exit()
def menu01():
  print("""
== OYUN MENÜSÜ ==

[1] Zar At
[2] Taş Kağıt Makas Oyna
[3] Sayı Tahmin Et
[4] Geri Dön
""")
  menu01 = input("Cevabınızı bekliyorum.\n")
  if menu01 == "1":
    menu011()
  elif menu01 == "2":
    menu012()
  elif menu01 == "3":
    menu013()
  elif menu01 == "4":
    menu0()

#Bağlantı Menüsü
def menu02():
  print("== BAĞLANTILAR ==\n")
  print("[1] GitHub\n[2] Geri Dön")
  sMenu02 = input("Cevabınızı bekliyorum.\n")
  if sMenu02 == "1":
    githubUrl = 'https://github.com/ArdaDnmz'
    webbrowser.open_new_tab(githubUrl)
    menu02()
  elif sMenu02 == "2":
    menu0()
#Oyun Oyna/Zar At
def menu011():
  programZar = False
    
  while programZar == False:
    x = input("Kaç yüzlü zar atmak istiyorsun?\n")
    sayı = random.randint(1,int(x))
    print("Sonuç:", sayı)
    zarDevam = input("Tekrar oynamak ister misin? y/n\n")
    if zarDevam == "y" or zarDevam == "Y":
      programZar = False
    elif zarDevam == "n" or zarDevam == "N":
      programZar = True
      menu01()
#Oyun Oyna/Taş Kağıt Makas
def menu012():
  durum = True;
  while durum:
    print("Seçim yapınız");
    print("[1] Taş");
    print("[2] Kağıt");
    secim = input("[3] Makas\n");
    botsecim = random.randint(1,3);
    #Berabere Durumları
    if secim == "1" and botsecim == 1:
      print("Rakibin Seçimi: Taş");
      print("Senin Seçimin: Taş");
      print("Sonuç: Berabere");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "2" and botsecim == 2:
      print("Rakibin Seçimi: Kağıt");
      print("Senin Seçimin: Kağıt");
      print("Sonuç: Berabere");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "3" and botsecim == 3:
      print("Rakibin Seçimi: Makas");
      print("Senin Seçimin: Makas");
      print("Sonuç: Berabere");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    #Kazanma Durumları
    elif secim == "1" and botsecim == 3:
      print("Rakibin Seçimi: Makas");
      print("Senin Seçimin: Kağıt");
      print("Sonuç: Kazandın");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "2" and botsecim == 1:
      print("Rakibin Seçimi: Taş");
      print("Senin Seçimin: Kağıt");
      print("Sonuç: Kazandın");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "3" and botsecim == 2:
      print("Rakibin Seçimi: Kağıt");
      print("Senin Seçimin: Makas");
      print("Sonuç: Kazandın");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    #Kaybetme Durumları
    elif secim == "1" and botsecim == 2:
      print("Rakibin Seçimi: Kağıt");
      print("Senin Seçimin: Taş");
      print("Sonuç : Kaybettin");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "2" and botsecim == 3:
      print("Rakibin Seçimi: Makas");
      print("Senin Seçimin: Kağıt");
      print("Sonuç: Kaybettin");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    elif secim == "3" and botsecim == 1:
      print("Rakibin Seçimi: Taş");
      print("Senin Seçimin: Makas");
      print("Sonuç: Kaybettin");
      tkmDevam = input("Tekrar oynamak ister misin? y/n\n")
      if tkmDevam == "y" or tkmDevam == "Y":
        durum = True
      elif tkmDevam == "n" or tkmDevam == "N":
        durum = False
        menu01()
    #1, 2 veya 3 sayısından başka bir sayı girilmesi durumunda hata verme durumu
    else:
        print("Lütfen geçerli bir cevap giriniz.")
#Oyun Oyna/Sayı Tahmin
def menu013():
  programSayiTahmin = True;

  denemeHakkı = None

  print("Sayı Tahmin Etme Oyunu'na Hoşgeldiniz.")

  while denemeHakkı == None:
    zorluk = input("""
  Zorluk Seçiniz
  [1] Kolay Mod
  [2] Normal Mod
  [3] Zor Mod
  """)
      
  #Kolay Mod Durumları
    if zorluk == "1":
      sayı = random.randint(1,50)
      denemeHakkı = 5
      
      print("Kolay Mod");
      print("1 ile 50 arasında bir sayı seçili.")
      print("5 deneme hakkın var.")
      print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
    while zorluk == "1":
      tahmin = input("Tahminde bulunun.\n")
      
      if int(sayı) == int(tahmin):
        print("Tebrikler. Cevabın doğru.")
        denemeHakkı = None
        zorluk = None
        sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
        if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
          programSayiTahmin = False
        elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
          programSayiTahmin = True
          menu01()
      elif int(sayı) != int(tahmin):
        denemeHakkı = denemeHakkı - 1
        print("Tahminin yanlış.")
        print("Kalan deneme hakkın:", denemeHakkı)
        if int(tahmin) > int(sayı):
          print("Tahminin seçili sayıdan büyük.")
        elif int(tahmin) < int(sayı):
          print("Tahminin seçili sayıdan küçük.")
        if denemeHakkı == 0:
          print("Kaybettin.")
          print("Cevap şuydu:", sayı)
          denemeHakkı = None
          zorluk = None
          sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
          if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
            programSayiTahmin = False
          elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
            programSayiTahmin = True
            menu01()

  #Normal Mod Durumları
    if zorluk == "2":
      sayı = random.randint(1,100)
      denemeHakkı = 5
      
      print("Normal Mod");
      print("1 ile 100 arasında bir sayı seçili.")
      print("5 deneme hakkın var.")
      print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
    while zorluk == "2":
      tahmin = input("""Tahminde bulunun.
      """)

      if int(sayı) == int(tahmin):
        print("Tebrikler. Cevabın doğru.")
        denemeHakkı = None
        zorluk = None
        sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
        if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
          programSayiTahmin = False
        elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
          programSayiTahmin = True
          menu01()
      elif int(sayı) != int(tahmin):
        denemeHakkı = denemeHakkı - 1
        print("Tahminin yanlış.")
        print("Kalan deneme hakkın:", denemeHakkı)
        if int(tahmin) > int(sayı):
          print("Tahminin seçili sayıdan büyük.")
        elif int(tahmin) < int(sayı):
          print("Tahminin seçili sayıdan küçük.")
        if denemeHakkı == 0:
          print("Kaybettin.")
          print("Cevap şuydu:", sayı)
          denemeHakkı = None
          zorluk = None
          sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
          if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
            programSayiTahmin = False
          elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
            programSayiTahmin = True
            menu01()
      
  #Zor Mod Durumları
    if zorluk == "3":
      sayı = random.randint(1,200)
      denemeHakkı = 5
      
      print("Zor Mod");
      print("1 ile 200 arasında bir sayı seçili.")
      print("5 deneme hakkın var.")
      print("Tahmininin seçili sayıdan büyük veya küçük olduğunu söyleyeceğiz.")
    while zorluk == "3":
      tahmin = input("""Tahminde bulunun.
      """)

      if int(sayı) == int(tahmin):
        print("Tebrikler. Cevabın doğru.")
        denemeHakkı = None
        zorluk = None
        sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
        if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
          programSayiTahmin = False
        elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
          programSayiTahmin = True
          menu01()
      elif int(sayı) != int(tahmin):
        denemeHakkı = denemeHakkı - 1
        print("Tahminin yanlış.")
        print("Kalan deneme hakkın:", denemeHakkı)
        if int(tahmin) > int(sayı):
          print("Tahminin seçili sayıdan büyük.")
        elif int(tahmin) < int(sayı):
          print("Tahminin seçili sayıdan küçük.")
        if denemeHakkı == 0:
          print("Kaybettin.")
          print("Cevap şuydu:", sayı)
          denemeHakkı = None
          zorluk = None
          sayiTahminDevam = input("Tekrar oynamak ister misin? y/n\n")
          if sayiTahminDevam == "y" or sayiTahminDevam == "Y":
            programSayiTahmin = False
          elif sayiTahminDevam == "n" or sayiTahminDevam == "N":
            programSayiTahmin = True
            menu01()


#Program başlangıç
menu0()

