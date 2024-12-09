#ШЕЛЛА

def shell_sort(arr):
    n = len(arr)
    g = n // 2  # Начальный шаг

    while g > 0:
        for i in range(g, n):
            val = arr[i]
            j = i
            # Вставляем arr[i] в отсортированную последовательность с шагом g
            while j >= g and arr[j - g] > val:
                arr[j] = arr[j - g]
                j -= g
            arr[j] = val

        g //= 2  # Уменьшаем шаг

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", shell_sort(seq))
