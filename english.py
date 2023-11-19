def english():
    count = 0
    points = 0

    user_input = input("Привет! Предлагаю проверить свои знания английского! Расскажи, как тебя зовут!\n")

    print(f'Привет,{user_input} , начинаем тренировку!')
    print("1 Задание")
    print("My name ___ Vova")

    user_input = input('Введите правильный ответ:\n')

    if user_input == "is":
        print("Ответ верный!\nВы получаете 10 баллов!\n")
        count += 1
        points += 10
    else:
        print("Неправильно. Правильный ответ: is\n")

    print("2 Задание")
    print("I ___ a coder")

    user_input = input('Введите правильный ответ:\n')

    if user_input == "am":
        print("Ответ верный!\nВы получаете 10 баллов!\n")
        count += 1
        points += 10
    else:
        print("Неправильно. Правильный ответ: am\n")

    print("3 Задание")
    print("I live ___ Moscow")

    user_input = input('Введите правильный ответ:\n')

    if user_input == "in":
        print("Ответ верный!\nВы получаете 10 баллов!\n")
        count += 1
        points += 10
    else:
        print("Неправильно. Правильный ответ: in\n")

    print(f'Вот и всё!\n'
          f'Вы ответили на {count} вопросов из 3 верно,\n'
          f'Вы заработали {points} баллов.'
          f'Это {(count*100)/3} процентов.')


english()
