#My solution

import random
def son_top(high, low= 1):

        print("Keling o'ylagan sonni topish o'ynaymiz!")
        computer_number = random.randint(low, high)
        user_number = input(f"{low} dan {high} gacha son o'yladim. Topa olasizmi?: ")
        user_number = int(user_number)
        count1 = 0
        won = False
        while not won:
            count1 += 1
            if user_number == computer_number:
                    print(f"TOPDINGIZ! {computer_number} sonini o'ylagan edim. {count1} ta tahmin bilan topdingiz. Tabriklayman!")
                    won = True
            elif user_number > computer_number:
                    user_number = int(input("Xato, men o'ylagan son bunda kichikroq. Yana harakat qiling: "))
            elif user_number < computer_number:
                    user_number = int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: "))
        return count1

def son_top_pc(high, low= 1):
    count2 = 0
    print(f"{low} dan {high} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    while True:
            computer_number = (low + high) // 2
            answer = input(f"Siz {computer_number} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? ")
            count2 += 1
            if answer == "T":
                print(f"Soningizni {count2} ta tahmin bilan topdim!")
                break
            elif answer == "+":
                low= computer_number + 1
            elif answer == "-":
                high = computer_number - 1
    return count2


while True:
    user_count = son_top(100)
    computer_count = son_top_pc(100)
    if user_count < computer_count:
        print(f"Tabriklayman! Siz {user_count} martada sonlarni to'g'ri topib g'olib bo'ldingiz")
    elif user_count > computer_count:
        print(f"Ura! Men {computer_count} martada sonlarni to'g'ri topib g'olib bo'ldim!")
    elif user_count == computer_count:
        print(f"Tabriklayman! Do'stlik g'alaba qozondi!")
    xohish = input("Yana o'ynashni xohlaysizmi? (xa uchun +, yo'q uchun -): ")
    if xohish == "-":
        break

#My solution end

"""
08/01/2021

Dasturlash asoslari

"SONNI TOPISH" O'YINI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import random


def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting:", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("Yutdingiz!")
            break

    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar


def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_pc = sontop_pc(x)
        taxminlar_user = sontop(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


play()


# son_top()