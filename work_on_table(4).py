table_of_attributes_and_values = [{"name_5": "Vitaly", "name_1": "Andrey", "name_2": "Mikhail", "name_3": "Alexandr", "name_4": "Ivan"},
                                  {"25": "name_1", "22": "name_2", "27": "name_3", "21": "name_4"},
                                  {"name_1": "teacher", "name_2": "teacher", "name_3": "vet", "name_4": "teacher"
                                   }]


def specify_search(table_of_attributes_and_values):
    while True:
        comparison = input("Какой знак вы хотите испльзовать: >(больше) или <(меньше)?")
        if comparison != ">" and comparison != "<":
            continue
        else:
            break
    return comparison


def search_by_profesion(table_of_attributes_and_values):
    while True:
        professions = []  # сюда закидываем учителей
        profession = input("Введите профессию искомого человека: ")
        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
            if indice == 3:
                for key in dictionary:
                    if dictionary[key] == profession:
                        professions.append(key)
        break
    return professions

def search_by_age(table_of_attributes_and_values):
    prof = search_by_profesion(table_of_attributes_and_values)
    names_of_people = []
    if len(prof) == 0:
        print("Людей с такой профессией нет в таблице\n\n\n")
    if len(prof) >= 1:
        names_of_professions_and_age = []
        peoples_age = input("Введите возраст искомого человека:")
        while True:
            wanna_compare = input("Хотите ли вы уточнить поиск с помощью математических символов (<,>)? Введите да или нет: ")
            if wanna_compare != "да" and wanna_compare != "нет":
                print("Вы можете использовать только слова да или нет!")
                continue
            else:
                break
        if wanna_compare == "да":
            sp_search = specify_search(table_of_attributes_and_values)
            if sp_search == ">":
                for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                    if indice == 2:
                        for key in dictionary:
                            for i in prof:
                                if i == dictionary[key] and key > peoples_age:
                                    names_of_professions_and_age.append(dictionary[key])
            if sp_search == "<":
                for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                    if indice == 2:
                        for key in dictionary:
                            for i in prof:
                                if i == dictionary[key] and key < peoples_age:
                                    names_of_professions_and_age.append(dictionary[key])
        if wanna_compare == "нет":
            for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                if indice == 2:
                    for key in dictionary:
                        for i in prof:
                            if i == dictionary[key] and key == peoples_age:
                                names_of_professions_and_age.append(dictionary[key])
        if len(names_of_professions_and_age) == 0:
            print("В данной таблице нет людей такого возраста, занимаюзихся данной профессией!")
        else:
            for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                if indice == 1:
                    for key in dictionary:
                        for i in names_of_professions_and_age:
                            if key == i:
                                names_of_people.append(dictionary[key])
            print(names_of_people)
        return names_of_people


def quitting_the_menu(table_of_attributes_and_values):
    while True:  # while True
        decision = input("Вы точно хотите выйти из меню? Введите: да или нет")
        if decision != "да" and decision != "нет":
            print("Вы можете использовать только да или нет")
            continue
        if decision == "да" or decision == "нет":  # что если напишет заглавную букву?, можно сильно сократить
            return decision


def reading_the_table_form_the_time(table_of_attributes_and_values):
    with open("table_of_attributes_and_values.txt","r") as file:
        reading_the_file = file.read()
    print(reading_the_file)
    return reading_the_file


def saving_the_table_in_the_file(table_of_attributes_and_values):
    with open("table_of_attributes_and_values.txt", "w") as file:
        file.write(str(table_of_attributes_and_values))
    print("Фвйл сохранен. Название файла: table_of_attributes_and_values.txt")

def show_the_sorted_table_of_attributes_and_values(table_of_attributes_and_values):
    sorted_dictionaries = []
    for dictionaries in table_of_attributes_and_values:
       sorting = {k: v for k, v in sorted(dictionaries.items(), key=lambda item: item[1])}
       sorted_dictionaries.append(sorting)
    return sorted_dictionaries


def deleting_element_drom_table(table_of_attributes_and_values):
    while True:
        lines_of_repeated_keys = []
        repeated_keys = 0
        delete_by_key = input("Введите название ключа, который Вы хотите удалить: ")
        for dictionary in table_of_attributes_and_values:
            for key in dictionary:
                if delete_by_key == key:
                    repeated_keys += 1
        if repeated_keys == 0:
            print("Введенного ключа нет в таблице!")
            continue
        if repeated_keys == 1:
            for dictionary in table_of_attributes_and_values:
                if delete_by_key in dictionary:
                    dictionary.pop(delete_by_key)
                print(table_of_attributes_and_values)
        if repeated_keys > 1:
            for idx, dictionary in enumerate(table_of_attributes_and_values, start=1):
                for key in dictionary:   # if delete_by_key in dictionary
                    if key == delete_by_key:
                        lines_of_repeated_keys.append(idx)
            print(lines_of_repeated_keys)
            while True:
                try:
                    what_repeated_key_you_want_to_delete = int(input("Введенные Вами ключ повторяются! Введите "
                                                                     "строку, из которой Вы хотите удалить ключ: "))
                except ValueError:
                    print("Вы ввели число из списка строк, в которых данный ключ встречается!")
                    continue
                if what_repeated_key_you_want_to_delete in lines_of_repeated_keys:
                    for idx, dictionary in enumerate(table_of_attributes_and_values, start=1):
                        if what_repeated_key_you_want_to_delete == idx:  # if delete_by_key in dictionary
                            for key in list(dictionary):
                                if key == delete_by_key:
                                    dictionary.pop(key)
                else:
                    print("Вы ввели номер строки, в котором данного элемента нет!")
                    continue
                break
            print(table_of_attributes_and_values)
            quit_or_continue = do_you_want_to_continue(table_of_attributes_and_values)
            if quit_or_continue == 1:
                continue
            if quit_or_continue == 2:
                break
    print(table_of_attributes_and_values)
    return table_of_attributes_and_values


def replacing_value(table_of_attributes_and_values):
    while True:
        value_found = 0
        replace_value = input("Введите значение ключ, которое Вы хотите изменить!")
        for dictionary in table_of_attributes_and_values:
            for key in dictionary:
                if replace_value == dictionary[key]:
                    value_found += 1
        if value_found == 0:
            print("Данного значения нет в таблице!")
            continue
        if value_found >= 1:
            replacing_v = input("На какое значение Вы хотите поменять данное значение?")
        if value_found == 1:            # функция замены одного значения
            for dictionary in table_of_attributes_and_values:
                for key in dictionary:
                    if replace_value == dictionary[key]:
                        dictionary.update({key: replacing_v})
        if value_found > 1:
            while True:
                list_of_keys_with_same_values_in_dictionary = []   # список с ключами, чьи значения повторяются
                list_of_repeated_values = []   # номера строк, где данное значение присутствует
                for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                    for key in dictionary:
                        if replace_value == dictionary[key]:
                            list_of_repeated_values.append(indice)
                repeated_lines_with_values = 0  # количество повторяющихся значений в одной строке
                if len(list(set(list_of_repeated_values))) >= 2:  # если == 1, то выводятся сразу же ключи
                    print("Строки, в которых данное значение повторяется :", list(set(list_of_repeated_values)))
                    try:
                        indice_and_line = int(input("Данное значение повторяется несколько раз! Введите номер строки, "
                                                    "в которой вы хотите поменять значение:"))
                    except ValueError:
                        print("Вы можете использовать только цифры!")
                        continue
                    if indice_and_line not in set(list_of_repeated_values):
                        print("В данной строке данного значения нет!")
                        continue
                    if indice_and_line in list_of_repeated_values:
                        for i in range(len(list_of_repeated_values)):
                            if list_of_repeated_values[i] == indice_and_line:
                                repeated_lines_with_values += 1
                    if repeated_lines_with_values == 1:
                        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                            if indice == indice_and_line:
                                for key in dictionary:
                                    if dictionary[key] == replace_value:
                                        dictionary.update({key: replacing_v})
                                        break
                    if repeated_lines_with_values > 1:
                        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                            if indice == indice_and_line:
                                for key in dictionary:
                                    if dictionary[key] == replace_value:
                                        list_of_keys_with_same_values_in_dictionary.append(key)
                        print("Ключи, значения которых повторяются в данной строке : ", list_of_keys_with_same_values_in_dictionary)
                        what_key_want_to_delete = input("Данное значение повторяется несколько раз в одной строке. "
                                                        "Значение какого ключа из данной строки вы хотите изменить?")
                        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                            if indice == indice_and_line:
                                for key in dictionary:
                                    if key == what_key_want_to_delete:
                                        dictionary.update({key: replacing_v})
                if len(list(set(list_of_repeated_values))) == 1 and len(list_of_repeated_values) >= 2:
                    for i in range(len(list(set(list_of_repeated_values)))):
                        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                            if list(set(list_of_repeated_values))[i] == indice:
                                for key in dictionary:
                                    if dictionary[key] == replace_value:
                                        list_of_keys_with_same_values_in_dictionary.append(key)
                    print(list_of_keys_with_same_values_in_dictionary)
                    what_key_want_to_delete_2 = input("Данное значение повторяется несколько раз в одной строке. "
                                                "Значение какого ключа из данной строки вы хотите изменить?")
                    for i in range(len(list(set(list_of_repeated_values)))):
                        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                            if list(set(list_of_repeated_values))[i] == indice:
                                for key in dictionary:
                                    if key == what_key_want_to_delete_2:
                                        dictionary.update({key: replacing_v})
                break
        break
    print(table_of_attributes_and_values)
    return table_of_attributes_and_values


def replacing_key(table_of_attributes_and_values):
    while True:
        replace_key = input("Название какого ключа Вы хотите изменить?")
        key_found = 0
        list_of_repeating_keys = []
        for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
            if replace_key in dictionary:
                list_of_repeating_keys.append(indice)
                key_found += 1
        if key_found == 0:
            print("Такого ключа нет в таблице!")
            continue
        while True:
            replacing_k = input("Какое название Вы хотите задать данному ключу?: ")
            if key_found == 1:
                for dictionary in table_of_attributes_and_values:
                    for key in list(dictionary):
                        if replace_key == key:
                            if replacing_k not in dictionary:
                                dictionary[replacing_k] = dictionary.pop(key)
                            else:
                                print("Данное название ключа уже есть в строке! Они не могут повторяться!")
                                continue
            break
        if key_found > 1:
            print(list_of_repeating_keys)
            while True:
                try:
                    line_you_want_to_change = int(input("В какой строке вы хотите изменить ключ?"))
                except ValueError:
                    print("Вы можете вводить только числа в диапазоне количества строк от 1 до", max(list_of_repeating_keys), "!")
                    continue
                for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                    if line_you_want_to_change == indice:
                        for key in list(dictionary):
                            if replace_key == key:
                                if replacing_k not in dictionary:
                                    dictionary[replacing_k] = dictionary.pop(key)
                                else:
                                    print("Данное название ключа уже есть в строке! Они не могут повторяться!")
                                    continue
                break
        break
    print(table_of_attributes_and_values)
    return table_of_attributes_and_values



def replacing_element_in_the_list_by_key_or_value(table_of_attributes_and_values):
    while True:
        try:
            replacing_by_key_or_value = int(input("Вы хотите изменить ключ или его значение? Введите 1 для "
                                                  "изменения ключа, 2 - для изменения значения ключа"))
        except ValueError:
            print("Вы можете использовать только цифры 1 или 2!")
            continue
        if replacing_by_key_or_value == 1:
            replace_key = replacing_key(table_of_attributes_and_values)
        if replacing_by_key_or_value == 2:
            replace_value = replacing_value(table_of_attributes_and_values)
        if replacing_by_key_or_value != 1 and replacing_by_key_or_value != 2:
            print("Вы можете вводить только цифры 1 и 2!")
            continue
        quit_or_continue = do_you_want_to_continue(table_of_attributes_and_values)
        if quit_or_continue == 1:
            continue
        if quit_or_continue == 2:
            break
    print(table_of_attributes_and_values)
    return table_of_attributes_and_values


def adding_to_new_line(table_of_attributes_and_values):
    while True:
        new_dictionary = {}
        while True:
            if len(new_dictionary) == 0:
                the_key_you_want_to_add = input("Какой ключ Вы хотите ввести?: ")
                the_value_you_want_to_add = input("Какое значение ключу Вы хотите задать?: ")
                new_dictionary[the_key_you_want_to_add] = the_value_you_want_to_add
                table_of_attributes_and_values.append(new_dictionary)
            if len(new_dictionary) > 1:
                for key in new_dictionary:
                    if the_key_you_want_to_add == key:
                        print("Данный ключ уже есть в строке! Измените название ключа!")
                        continue
            break
        break
    print(table_of_attributes_and_values)
    return table_of_attributes_and_values


def adding_to_existing_line(table_of_attributes_and_values):
    number_of_lines = len(table_of_attributes_and_values)
    print(table_of_attributes_and_values)
    print("Количество строк: ", number_of_lines)
    while True:
        try:
            line_you_want_to_add_to = int(input("В какую строку вы хотите добавить значение?:"))  # для удобства
        # нужно вывести все строки, while True чтобы при ошибке возвращало сюда
        except ValueError:
            print("Вы можете вводить только числа в диапазоне количества строк от 1 до", number_of_lines, "!")
            continue
        if line_you_want_to_add_to <= number_of_lines and line_you_want_to_add_to >= 1:
            for indice, dictionary in enumerate(table_of_attributes_and_values, start=1):
                if line_you_want_to_add_to == indice:
                    while True:  # функция (введение ключа)
                        enter_the_key = input("Введите название ключа: ")
                        if enter_the_key in dictionary:
                            print("Данный ключ уже есть в строке! Ключи не могут повторяться в одной "
                                  "строке! Введите другой ключ или выберите другую строку!")
                            continue
                        else:
                            print("Введенный Вами ключ: ", enter_the_key)
                            enter_the_value = input("Введите значение ключа:")
                            dictionary[enter_the_key] = enter_the_value
                            break  # конец функции(введение ключа)
        else:
            print("Вы можете вводить только числа в диапазоне количества строк от 1 до", number_of_lines, "!")
            continue
        print(table_of_attributes_and_values)
        return table_of_attributes_and_values


def add_element_to_the_table(table_of_attributes_and_values):
    while True:
        try:
            where_you_want_to_add = int(input("Вы хотите добавить значение в существующую строку или в новую? 1 - "
                                              "в существующую, 2 - в новую"))
        except ValueError:
            print("Вы можете использовать только цифры 1 или 2!")
            continue
        if where_you_want_to_add < 1 or where_you_want_to_add > 2:
            print("Вы можете использовать только цифры 1 или 2!")
            continue
        if where_you_want_to_add == 1:
            add_to_exist_line = adding_to_existing_line(table_of_attributes_and_values)
        if where_you_want_to_add == 2:
            add_to_new_line = adding_to_new_line(table_of_attributes_and_values)
        quit_or_continue = do_you_want_to_continue(table_of_attributes_and_values)
        if quit_or_continue == 1:
            continue
        if quit_or_continue == 2:
            break
    return table_of_attributes_and_values


def do_you_want_to_continue(table_of_attributes_and_values):
    while True:
        try:
            continue_or_quit = int(input("Вы хотите продолжить осуществлять данную операцию над таблицей? 1 - да, 2 - выход в"
                                 " меню"))
        except ValueError:
            print("Вы можете использовать только цифры 1 и 2!")
            continue
        if continue_or_quit == 1 or continue_or_quit == 2:
            return continue_or_quit
        if continue_or_quit !=1 or continue_or_quit != 2:
            continue


def menu(table_of_attributes_and_values):
    while True:
        print(table_of_attributes_and_values, "\n\n\n")
        print("0 — выйти\n1 — добавить элемент\n2 — заменить элемент\n3 - удалить элемент\n4 — вывести\n5 — вывести в "
              "отсортированном виде\n6 — сохранить таблицу в файл\n7 — загрузить таблицу из файла\n8 - поиск"
              "\nвведите цифру для выбора пункта меню:")
        try:
            item_of_the_menu = int(input())
        except ValueError:
            print("Вы можете использовать только числа от 0 до 8!")
            continue
        if item_of_the_menu >= 0 and item_of_the_menu <= 8:
            if item_of_the_menu == 0:
                decision_quit_or_not = quitting_the_menu(table_of_attributes_and_values)
                if decision_quit_or_not == "нет":
                    continue
                if decision_quit_or_not == "да":
                    print("\n\n\nДо свидания!\n\n\n")
                    break
            elif item_of_the_menu == 1:
                table_of_attributes_and_values_with_added_value = add_element_to_the_table(table_of_attributes_and_values)
            elif item_of_the_menu == 2:
                table_of_attributes_and_values_with_replaced_elements = replacing_element_in_the_list_by_key_or_value(table_of_attributes_and_values)
            elif item_of_the_menu == 3:   #  сделать так, чтобы удалялось значение или ключ
                table_of_attributes_and_values_with_deleted_value = deleting_element_drom_table(table_of_attributes_and_values)
            elif item_of_the_menu == 4:
                print(table_of_attributes_and_values)
            elif item_of_the_menu == 5:
                sorted_table = show_the_sorted_table_of_attributes_and_values(table_of_attributes_and_values)
            elif item_of_the_menu == 6:
                saving_file = saving_the_table_in_the_file(table_of_attributes_and_values)
            elif item_of_the_menu == 7:
                reading_file = reading_the_table_form_the_time(table_of_attributes_and_values)
            elif item_of_the_menu == 8:
                search_by_a = search_by_age(table_of_attributes_and_values)
        else:
            print("Вы можете использовать только числа от 0 до 8!, хуесос")
            print("Быдло ебаное!")
            continue
calling_for_the_menu = menu(table_of_attributes_and_values)