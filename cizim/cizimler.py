import turtle
import random
def cizimlermenu():
    print("╔═════════════════════╗")
    print("║    Çizimler         ║")
    print("║                     ║")
    print("║  1-Kare             ║")
    print("║  2-Üçgen            ║")
    print("║  3-Beşgen           ║")
    print("║  4-Altıgen          ║")
    print("║  5-Sekizgen         ║")
    print("║  6-Ana Menü         ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print()
    secim=input("Yapmak istediğiniz işlemin başındaki sayıyı yazınız:")
    if secim=="1":
        renkler=["red","blue","magenta","yellow","pink"]
        for a in range (4):
            # print(renkler[a])
            # turtle.color(renkler[a])
            turtle.color(random.choice(renkler))
            turtle.forward(100)
            turtle.right(90)
        input()
        cizimlermenu()
    elif secim=="2":
            renkler=["red","blue","magenta","yellow","pink"]
            for a in range (3):
                # print(renkler[a])
                # turtle.color(renkler[a])
                turtle.color(random.choice(renkler))
                turtle.forward(100)
                turtle.right(120)
            input()
            cizimlermenu()

    elif secim=="3":
            renkler=["red","blue","magenta","yellow","pink"]
            for a in range (5):
                # print(renkler[a])
                # turtle.color(renkler[a])
                turtle.color(random.choice(renkler))
                turtle.forward(100)
                turtle.right(72)
            input()
            cizimlermenu()

    elif secim=="4":
            renkler=["red","blue","magenta","yellow","pink"]
            for a in range (6):
                # print(renkler[a])
                # turtle.color(renkler[a])
                turtle.color(random.choice(renkler))
                turtle.forward(100)
                turtle.right(60)
            input()
            ccizimlermenu()

    elif secim=="5":
            renkler=["red","blue","magenta","yellow","pink"]
            for a in range (8):
                # print(renkler[a])
                # turtle.color(renkler[a])
                turtle.color(random.choice(renkler))
                turtle.forward(100)
                turtle.right(45)
            input()
            cizimlermenu()

    elif secim=="6":
        print("Ana Menü'ye dönülüyor.")
        return
    else:
        print("Lütfen menüde bulunan geçerli bir sayı giriniz.")