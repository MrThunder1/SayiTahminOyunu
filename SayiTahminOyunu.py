import random

rastgele = random.randint(1,100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında tuttuğum sayıyı bilmek için bir sayı giriniz (oyundan çıkmak için '0' a basınız): "))
    if (sayi == 0):
        print("oyundan çıkıldı")
        break
    if (sayi < rastgele):
        print("Daha büyük bir sayı giriniz")
        continue
    if (sayi > rastgele):
        print("Daha küçük bir sayı giriniz")
        continue
    else:
        print("Tebrikler doğru bildiniz")
        print("Rastgele seçilen sayı: {}".format(rastgele))
        print("Tahmin sayınız: {}".format(sayac))
        break