def get_info (): #функция заполнения телефонной книги
    info = []
    info.append({'Фамилия': input("Введите фамилию: ")})  # x [0]['a']= 1
    info.append({'Имя': input("Введите имя: ")})
    info.append({'Телефон': ""})
    valid = False
    while not valid:
        try:
            info[2] = {"Телефон": input("Введите номер телефона: ")}
            if len(info[2]["Телефон"]) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                info[2]["Телефон"] = int(info[2]["Телефон"])
                valid = True
        except:
            print("Номер телефона должен состоять только из цифр")
    info.append({'Описание': input("Введите описание: ")})
    info.append({'Зароботная плата (тыс. руб.)': int(input("Введите размер зароботной платы: "))})
    print(info)
    return info





