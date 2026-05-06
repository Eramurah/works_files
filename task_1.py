try:
    with open("input.txt", "w", encoding='utf-8') as file:
        file.write("""a
2 b
3 c
4""")

        file.close()

except Exception as ex:
    print(ex)

try:
    counter = open("input.txt", "r", encoding='utf-8') #Строки

    a = len(counter.readlines())
    a = "Количество строк: " + str(a) + "\n"

    counter.close()

    with open("input.txt", "r", encoding='utf-8') as counter: #Слова
        count = 0
        for line in counter:
            count += len(line.split())

        counter.close()

    count = "Количество слов: " + str(count)

    try:
        with open("statistics.txt", "w", encoding='utf-8') as file_1:
            file_1.write(str(a) + str(count))

            file_1.close()

    except Exception as ex:
        print(ex)

    counter.close()

except Exception as ex:
    print(ex)
