import random
takror = True
while takror:
    print("Keling o'ylagan sonni topish o'ynaymiz!")
    computer_number = random.randint(1, 10)
    user_number = input("1 dan 10 gacha son o'yladim. Topa olasizmi?: ")
    user_number = int(user_number)
    count = 0
    won = False
    while user_number < computer_number:
            kattaroq = input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
            guess = int(kattaroq)
            count += 1
            if computer_number == guess:
                print(f"TOPDINGIZ! {computer_number} sonini o'ylagan edim. {count} tahminda topdingiz! Tabriklayman!")
                won = True
                break
    while user_number > computer_number:
            kichikroq = input("Xato, men o'ylagan son bunda kichikroq. Yana harakat qiling: ")
            guess2 = int(kichikroq)
            count += 1
            if guess2 == computer_number:
                print(f"TOPDINGIZ! {computer_number} sonini o'ylagan edim. {count} ta tahmin bilan topdingiz. Tabriklayman!")
                won = True
                break
    if user_number == computer_number:
            print(f"TOPDINGIZ! {computer_number} sonini o'ylagan edim. 1 ta tahmin bilan topdingiz. Tabriklayman!")
            won = True
    if won:
        xohish = input("Yana o'ynashni xohlaysizmi? (xa uchun +, yo'q uchun -): ")
        if xohish == "-":
            break