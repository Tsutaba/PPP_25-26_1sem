def filter_letters(input_string):
    # input_string - входная строка состоящая из латинских букв
    # Словарь для подсчета букв
    count = {}

    # Подсчет количества строчных и заглавных букв
    for symbol in input_string:
        if symbol.isalpha():  # Проверяем, является ли символ буквой
            lower_symbol = symbol.lower()  # Приводим символ к строчному регистру
            if lower_symbol not in count:
                count[lower_symbol] = [0, 0]  # [количество строчных, количество заглавных]

            # Увеличиваем счетчик
            if symbol.islower():
                count[lower_symbol][0] += 1  # Увеличиваем счетчик строчных
            else:
                count[lower_symbol][1] += 1  # Увеличиваем счетчик заглавных

    # Формируем новую строку, исключая буквы, где строчные > заглавные
    result = []
    for symbol in input_string:
        if symbol.isalpha():
            lower_symbol = symbol.lower()  # Приводим к строчному регистру
            if count[lower_symbol][0] > count[lower_symbol][1]:  # Проверяем условия
                continue  # Если условия нарушены, пропускаем букву
        result.append(symbol)  # Добавляем букву, если она проходит проверку

    return ''.join(result)  # Объединяем список символов в строку


def main():
    input_string = input("Введите строку, состоящую из латинских букв: ")

    # Проверка на некорректные символы
    if not all(symbol.isalpha() or symbol.isspace() for symbol in input_string):
        print("Ошибка: строка должна содержать только латинские буквы и пробелы.")
        return

    # Фильтруем буквы
    filtered_string = filter_letters(input_string)

    print("Отфильтрованная строка:", filtered_string)

if __name__ == "__main__":
    main() # Ваш код здесь
