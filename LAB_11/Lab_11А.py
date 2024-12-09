#БЫСТРАЯ

def qsort(arr):
    if len(arr) <= 1:  # Базовый случай
        return arr
    else:
        piv = arr[-1]  # Опорный элемент
        l = [x for x in arr[:-1] if x <= piv]  # Меньшие или равные опорному
        r = [x for x in arr[:-1] if x > piv]  # Больше опорного

        # Рекурсивно сортируем и объединяем
        return qsort(l) + [piv] + qsort(r)

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", qsort(seq))

