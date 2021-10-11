
import random
balance = 0
plushka1 = 0
plushka2 = 0
plushka3 = 0

def primer():
    global balance
    a=random.randint(50, 100)
    b=random.randint(10, 49)
    c=int(a + b)
    primer = input("Сколько будет " + str(a) + " + " + str(b) + ": ")
    if primer == str(c):
        balance += 50
        print("Ты решил пример, и получил 50 монет, вот твой баланс - " + str(balance))

    else:
        print("Ты решил пример неправильно, в следующий раз повезёт!")


nickname = input("Кто ты, путешественник?: ")
while True:
    menu = input(str(nickname) + ", ты попал в главное меню, выбери куда ты хочешь переместиться:\n1 - Настройки\n2 - Работа\n3 - Информация о cебе:\n4 - Магазин аксессуаров: ")
    if menu == "1":
        config = input("Ты находишься в настройках, выбери куда ты хочешь переместиться\n1 - Главное меню\n2 - Изменить никнейм: ")    
        if config == "1":
            continue
        elif config == "2":
            nickname = input("Введи свой новый никнейм: ")
            continue
    elif menu == "2":
        work = input( "Ты находишься на работе, (Зарабатывать ты можешь решая примеры) выбери куда ты хочешь переместиться:\n1 - Главное меню\n2 - Начать работу: ")
        if work == "1":
            continue
        if work == "2":
            primer()
    elif menu == "3":
        input("Информация о тебе:\nТвой игровой ник - " + str(nickname) + "\nТвой баланс - " + str(balance) + "\nЧтобы выйти в меню нажми клавишу Enter")

    elif menu == "4":
        plushki_privet = input("Привет, ты попал в магазин аксессуаров, тут ты можешь купить себе разные приколюхи.\n1 - Выйти в главное меню\n2 - Посмотреть товары: ")
        if plushki_privet == "1":
            continue
        elif plushki_privet == "2":
            vibor_plushek = input("В наличии у нас есть:\n1 - Красная кепка\n2 - Оранжевое худи\n3 - Пляжные шорты(плавки)\n4 - Выйти в главное меню: ")
            if vibor_plushek == "4":
                continue
            elif vibor_plushek == "3":
                pokupka_plushki1 = input("Ты точно хочешь приобрести эти шорты? Цена за них 75 монет\n1 - Приобрести кепку\n2 - Выйти в главное меню: ")
                if pokupka_plushki1 == "2":
                    continue
                elif pokupka_plushki1 == "1":
                    if balance >= 75:
                        plushka3 = 1
                        pokupka_True = input("Круто!, теперь у тебя есть пляжные шорты,\nчтобы выйти в главное меню нажми Enter")
                        balance -= 75
                    elif balance < 75:
                        pokupka_False = input("Недостаточно монет чтобы приобрести этот товар.\nЧтобы выйти в главное меню нажми Enter")
                
            elif vibor_plushek == "1":
                pokupka_plushki1 = input("Ты точно хочешь приобрести эту красную кепку? Цена за неё 25 монет\n1 - Приобрести шорты\n2 - Выйти в главное меню: ")
                if pokupka_plushki1 == "2":
                    continue
                elif pokupka_plushki1 == "1":
                    if balance >= 25:
                        plushka1 = 1
                        pokupka_True = input("Круто!, теперь у тебя есть красная кепка,\nчтобы выйти в главное меню нажми Enter")
                        balance -= 25
                    elif balance < 25:
                        pokupka_False = input("Недостаточно монет чтобы приобрести этот товар.\nЧтобы выйти в главное меню нажми Enter")
            
            
            elif vibor_plushek == "2":
                pokupka_plushki1 = input("Ты точно хочешь приобрести это Оранжевое худи? Цена за неё 100 монет\n1 - Приобрести худи\n2 - Выйти в главное меню: ")
                if pokupka_plushki1 == "2":
                    continue
                elif pokupka_plushki1 == "1":
                    if balance >= 100:
                        plushka2 = 1
                        pokupka_True = input("Круто!, теперь у тебя есть Оранжевое худи,\nчтобы выйти в главное меню нажми Enter")
                        balance -= 100
                    elif balance < 100:
                        pokupka_False = input("Недостаточно монет чтобы приобрести этот аксессуар.\nЧтобы выйти в главное меню нажми Enter")

                    
            elif menu == "3":
                print("Информация о тебе:\nТвой игровой ник - " + str(nickname) + "\nТвой баланс - " + str(balance) + )
                if plushka1 == 1:
                    print(plushka1)