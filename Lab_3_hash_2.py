def hash(key):
    # Хэш-функция: порядковый номер первой буквы ключа
    first_letter = str(key)[0].lower()
    if first_letter.isalpha() and first_letter.isascii():
        return ord(first_letter) - ord('a') + 1
    return 0  # Если первый символ не буква, вернуть 0


class HashTable:
    def __init__(self):
        self.hash_table = {}

    def insert_into_table(self, structure):
        for key, value in structure.items():
            # Расчет индексов для трех хэш-таблиц с использованием разных хэш-функций

            # Хэш-функция 1: размер строки ключа
            index = hash(key)

            # Если index1 еще не существует в хэш-таблице 1
            if index not in self.hash_table:
                # Создание новой записи с ключом index1 и значением в виде словаря
                self.hash_table[index] = [value]
            else:
                # Добавление нового значения к уже существующему значению
                self.hash_table[index].append(value)

    def print_sorted_table(self):
        # Вывод отсортированных хэш-таблиц
        print("Хэш-таблица:", {k: sorted(map(str, v)) for k, v in sorted(self.hash_table.items())})


# Структура с фамилиями учеников в качестве ключей и оценками в виде списков
students_data = {
    "Ivanov": [5, 4, 5],
    "Sidorov": [4, 3, 5],
    "Kopotilov": [5, 5, 5]
}

hash_table = HashTable()
hash_table.insert_into_table(students_data)
hash_table.print_sorted_table()
