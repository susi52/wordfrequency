text = input("Введите строку: ")

words = text.lower().split()

word_count = {} # Словарь для подсчёта

for word in words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1   

for word, count in word_count.items():
    print(f"{word} -> {count}")

with open("result.txt", "w", encoding="utf-8") as f:
    for word, count in word_count.items():
        f.write(f"{word} -> {count}\n")

print("Результат сохранён в result.txt")
