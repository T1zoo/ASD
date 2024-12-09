#СЛИЯНИЕМ

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Середина массива
        left = arr[:mid]  # Левая половина
        right = arr[mid:]  # Правая половина

        # Рекурсивное разделение
        merge_sort(left)
        merge_sort(right)

        # Индексы для слияния элементов левой и правой половин
        i = j = k = 0

        # Слияние левой и правой половин
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы из левой половины
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы из правой половины
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", merge_sort(seq))

