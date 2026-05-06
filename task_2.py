a = input("Введите слово: "); b = 0

with open("text.txt", "w", encoding='UTF-8') as file:
    file.write("""Bobr
Car
Apple
Car""")

    file.close()

try:
    find = open("text.txt", "r")

    for i in find:
        if str(a) == i or str(a) + "\n" == i:
            b += 1

    find.close()

    if b != 0:
        try:
            print(f"""\nСлово найдено. \nВстречается {b} раз(а).""")
            with open("search_results.txt", "w", encoding='UTF-8') as file:
                file.write(f"""Слово найдено. \nВстречается {b} раз(а).""")

                file.close()

        except Exception as ex:
            print(ex)

    else:
        try:
            print(f"""\nСлово не найдено. \nВстречается {b} раз(а).""")
            with open("search_results.txt", "w", encoding='UTF-8') as file:
                file.write(f"""Слово не найдено. \nВстречается {b} раз(а).""")

                file.close()

        except Exception as ex:
            print(ex)

except Exception as ex:
    print(ex)
