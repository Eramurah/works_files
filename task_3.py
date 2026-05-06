with open("file1.txt", "w", encoding='UTF-8') as file1:
    file1.write("""slovo1""")
    file1.close()

with open("file2.txt", "w", encoding='UTF-8') as file2:
    file2.write("""slovo2""")
    file2.close()

with open("file3.txt", "w", encoding='UTF-8') as file3:
    file3.write("""slovo3""")
    file3.close()

try:
    i = 0
    with open("combined.txt", "w", encoding='UTF-8') as file:
        file.write("""=== Содержимое file1.txt ===\n""")

        with open("file1.txt", "r", encoding='UTF-8') as file1:
            file.write(file1.read())
            file.write("\n\n")
            file1.close()

        file.write("""=== Содержимое file2.txt ===\n""")

        with open("file2.txt", "r", encoding='UTF-8') as file2:
            file.write(file2.read())
            file.write("\n\n")
            file2.close()

        file.write("""=== Содержимое file3.txt ===\n""")

        with open("file2.txt", "r", encoding='UTF-8') as file3:
            file.write(file3.read())
            file.write("\n\n")
            file3.close()

        file.close()

except Exception as ex:
    print(ex)
