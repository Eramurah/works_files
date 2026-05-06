with open("secret.txt", "w", encoding='UTF-8') as file1:
    file1.write("""Текст""")
    file1.close()

with open("secret.txt", "r", encoding='UTF-8') as file1:
    result1 = ""
    for i in file1.read():
        if 'а' <= i <= 'я':
            new_code = ord(i) + 3
            if new_code > ord('я'):
                new_code = ord('а') + (new_code - ord('я') - 1)
            result1 += chr(new_code)

        elif 'А' <= i <= 'Я':
            new_code = ord(i) + 3
            if new_code > ord('Я'):
                new_code = ord('А') + (new_code - ord('Я') - 1)
            result1 += chr(new_code)

        else:
            result1 += i

    file1.close()

with open("encrypted.txt", "w", encoding='UTF-8') as file2:
    file2.write(result1)
    file2.close()

with open("encrypted.txt", "r", encoding='UTF-8') as file2:
    result2 = ""
    for i in file2.read():
        if 'а' <= i <= 'я':
            new_code = ord(i) - 3
            if new_code < ord('а'):
                new_code = ord('я') - (ord('а') - new_code - 1)
            result2 += chr(new_code)

        elif 'А' <= i <= 'Я':
            new_code = ord(i) - 3
            if new_code < ord('А'):
                new_code = ord('Я') - (ord('А') - new_code - 1)
            result2 += chr(new_code)

        else:
            result2 += i

    file1.close()

with open("decrypted.txt", "w", encoding='UTF-8') as file3:
    file3.write(result2)
    file3.close()
