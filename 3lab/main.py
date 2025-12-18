import os

def recursive_directory_walk(path, result=None, step_analysis=None):
    if result is None:
        result = {}
    if step_analysis is None:
        step_analysis = []

    # Добавляем текущий путь в анализ шагов
    step_analysis.append(path)

    # Список всех файлов и директорий в текущем каталоге
    items = os.listdir(path)

    # Проходим по всем элементам в текущем каталоге
    for item in items:
        # Полный путь к элементу
        full_path = os.path.join(path, item)

        # Проверяем, является ли элемент директорией
        if os.path.isdir(full_path):
            # Если это директория, добавляем её в результат как вложенный словарь
            result[item] = {}
            # Вызываем функцию для обхода этой директории
            recursive_directory_walk(full_path, result[item], step_analysis)
        else:
            # Если это файл, добавляем его в результат как элемент списка
            if 'files' not in result:
                result['files'] = []
            result['files'].append(item)

    return result, step_analysis

# Пример
directory_path = r"C:\Презентации"
structure, analysis = recursive_directory_walk(directory_path)

# Вывод
print("Структура директории:")
print(structure)
print("\nПошаговый анализ обхода:")
print(analysis)

if __name__ == "__main__":
    pass # Ваш код здесь
