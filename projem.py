print("\033[1;40;40m")

import hesapmak.hesapmakinesi
import cizim.cizimler
import takvim.takvim
import resim.resimler
import notlar.nothesaplama

def projem():

    print("╔═════════════════════╗")
    print("║     ÇALIŞMALAR      ║")
    print("║                     ║")
    print("║  1-Hesap Makinesi   ║")
    print("║  2-Cizimler         ║")
    print("║  3-Takvim           ║")
    print("║  4-Resimler         ║")
    print("║  5-Not Hesaplama    ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Bir sayı giriniz;")

    if secim == "1" : 
        hesapmak.hesapmakinesi.hesapmakinesimenu()
        projem()
    
    elif secim == "2" : 
        cizim.cizimler.cizimlermenu()
        projem()

    elif secim == "3" : 
        takvim.takvim.takvimmenu()
        projem()

    elif secim == "4" : 
        resim.resimler.resimlermenu()
        projem()

    elif secim == "5" : 
        notlar.nothesaplama.nothesaplamamenu()
        projem()

    else : 
        print("Lütfen geçerli bir sayı giriniz.")
        projem()

projem()

