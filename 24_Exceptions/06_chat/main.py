

with open('history.txt', 'w+') as history:
    while True:
        user_name = input("Введите ваше имя: ")
        print(f"{user_name}, выберите действие:")
        print("1. Посмотреть текущий текст чата")
        print("2. Отправить сообщение")
        ans = input("1 или 2: ")

        try:
            int(ans)
        except ValueError:
            print("Что-то пошло нет так. Начнем сначала")

        if int(ans) == 1:
            for line in history:
                print(line, end="")
            print()

        elif int(ans) == 2:
            user_mes = input("Введите ваше сообщение: ")
            user_mes = f"{user_name}: {user_mes}"
            print(user_mes, file=history)

        else:
            print("Только 1 или 2!!!")