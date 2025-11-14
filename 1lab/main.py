from collections import Counter


def analyze_text(text):
    text = text.lower()

    # Убираем небуквенные символы для подсчета букв
    letters = [simbol for simbol in text if simbol.isalpha()]

    # Разбиение текста на слова
    words = text.split()

    # Подсчет частоты встречаемости букв
    letter_frequency = Counter(letters)

    # Подсчет частоты встречаемости слов
    word_frequency = Counter(words)

    return letter_frequency, word_frequency


def main():
    # Считываем текст от пользователя
    text = input("Введите длинную строку текста: ")

    # Анализ текста
    letter_frequency, word_frequency = analyze_text(text)

    # Получаем 5 самых популярных букв
    most_common_letters = letter_frequency.most_common(5)
    print("\n5 самых популярных букв:")
    for letter, freq in most_common_letters:
        print(f"'{letter}': {freq} раз")

    # Получаем 5 самых популярных слов
    most_common_words = word_frequency.most_common(5)
    print("\n5 самых популярных слов:")
    for word, freq in most_common_words:
        print(f"'{word}': {freq} раз")

if __name__ == "__main__":
    main() # Ваш код здесь
