def comb_sort(arr):
    n = len(arr)
    gap = n
    factor = 1.3  # Коэффициент уменьшения шага
    sorted = False

    while not sorted:
        # Уменьшаем шаг для следующего прохода
        gap = max(1, int(gap / factor))
        sorted = gap == 1  # Предполагаем, что массив отсортирован при gap = 1

        # Проходим по массиву с текущим шагом
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                # Если элементы не в порядке, меняем их
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False  # Устанавливаем флаг, что сортировка не завершена

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", comb_sort(seq))
