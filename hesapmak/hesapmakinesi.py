def hesapmakinesimenu():
    print("╔═══════════════════════════╗")
    print("║    HESAP MAKİNESİ         ║")
    print("║                           ║")
    print("║   1-Toplama               ║")
    print("║   2-Çıkarma               ║")
    print("║   3-Çarpma                ║")
    print("║   4-Bölme                 ║")
    print("║                           ║")
    print("║    Seçiminiz Nedir?       ║")
    print("╚═══════════════════════════╝")

    secim = input()

    print(secim,"seçtiniz.")
    if secim ==1 :
        print("1 seçtiniz, Toplama yapılacak.")
    if secim ==2 :
        print("2 seçtiniz, Çıkarma yapılacak.")
    if secim ==3 :
        print("3 seçtiniz, Çarpma yapılacak.") 
    if secim ==4 :
        print("4 seçtiniz, Bölme yapılacak.")   
    else :
        print("Lütfen geçerli bir sayı girin!")
        
        secim = int(input())
        