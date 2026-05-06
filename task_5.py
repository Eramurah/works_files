with open("words.txt", "w", encoding='UTF-8') as file1:
    file1.write("""Слово
абв
АБВГ
множество""")
    file1.close()

with open("words.txt", "r", encoding="utf-8") as file:
    words = [line.strip() for line in file if line.strip()]
    file.close()

sorted_alphabetically = sorted(words)

sorted_by_length = sorted(words, key=len)

sorted_reverse = sorted(words, reverse=True)

with open("sorted_alphabetically.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(sorted_alphabetically))
    file.close()

with open("sorted_by_length.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(sorted_by_length))
    file.close()

with open("sorted_reverse.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(sorted_reverse))
    file.close()
