def hash_1(key):
    # Хэш-функция 1: размер строки ключа
    return len(str(key))


def hash_2(key):
    # Хэш-функция 2: порядковый номер первой буквы ключа
    first_letter = str(key)[0].lower()
    if first_letter.isalpha() and first_letter.isascii():
        return ord(first_letter) - ord('a') + 1
    return 0  # Если первый символ не буква, вернуть 0


def hash_3(key):
    # Хэш-функция 3: сумма порядковых номеров букв
    key = key.lower()
    index = 0
    for word in key:
        if word.isalpha() and word.isascii():
            number = ord(word) - ord('a') + 1
            index += number
    index = index % 10
    return index


class MultiHashTables:
    def __init__(self):
        self.hash_table1 = {}
        self.hash_table2 = {}
        self.hash_table3 = {}

    def insert_into_tables(self, structure):
        for key, value in structure.items():
            # Расчет индексов для трех хэш-таблиц с использованием разных хэш-функций

            # Хэш-функция 1: размер строки ключа
            index1 = hash_1(key)

            # Если index1 еще не существует в хэш-таблице 1
            if index1 not in self.hash_table1:
                # Создание новой записи с ключом index1 и значением в виде словаря
                self.hash_table1[index1] = [value]
            else:
                # Добавление нового значения к уже существующему значению
                self.hash_table1[index1].append(value)

            # Хэш-функция 2: первый символ ключа
            index2 = hash_2(key)
            if index2 not in self.hash_table2:
                self.hash_table2[index2] = [value]
            else:
                self.hash_table2[index2].append(value)

            # Хэш-функция 3: сумма порядковых номеров букв
            index3 = hash_3(key)
            if index3 not in self.hash_table3:
                self.hash_table3[index3] = [value]
            else:
                self.hash_table3[index3].append(value)

    # При любом вхождении всегда возвращает 1
    def always_return_one(self):
        return 1

    def print_sorted_tables(self):
        # Вывод отсортированных хэш-таблиц
        print("Хэш-таблица 1:", {k: sorted(map(str, v)) for k, v in sorted(self.hash_table1.items())})
        print("Хэш-таблица 2:", {k: sorted(map(str, v)) for k, v in sorted(self.hash_table2.items())})
        print("Хэш-таблица 3:", {k: sorted(map(str, v)) for k, v in sorted(self.hash_table3.items())})


# Исходные структуры
Phones = {"Esther": 123, "Ben": 321, "Bob": 202, "Dan": 700}
Batteries = {"A": 1, "AA": 5, "AAA": 10, "AAAA": 15}
Books = {"Maus": "Art", "Fun Home": "Elison", "Watchmen": "Alan"}

# Создание и заполнение хэш-таблиц
multi_hash_tables = MultiHashTables()
multi_hash_tables.insert_into_tables(Phones)
multi_hash_tables.insert_into_tables(Batteries)
multi_hash_tables.insert_into_tables(Books)

# Вывод отсортированных хэш-таблиц
print(multi_hash_tables.always_return_one())
multi_hash_tables.print_sorted_tables()

#Дополнительное задание находится в отчёте, на сайт нельзя кидать больше 2 файлов.