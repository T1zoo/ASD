#ПОРАЗРЯДНАЯ

def count_sort_radix(arr, exp):
    n = len(arr)
    out = [0] * n  # Массив для результата сортировки по текущему разряду
    cnt = [0] * 10  # Счётчик для цифр (0-9)

    # Подсчитываем количество вхождений каждой цифры в текущем разряде
    for num in arr:
        idx = num // exp
        cnt[idx % 10] += 1

    # Преобразуем cnt так, чтобы cnt[i] содержал позицию этой цифры в out
    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    # Заполняем out числами по текущему разряду
    for num in reversed(arr):
        idx = num // exp
        out[cnt[idx % 10] - 1] = num
        cnt[idx % 10] -= 1

    # Копируем отсортированные числа в исходный массив
    for i in range(n):
        arr[i] = out[i]

def radix_sort(arr):
    # Находим максимальное число, чтобы определить количество разрядов
    max_num = max(arr)

    # Сортируем каждый разряд с помощью подсчёта
    exp = 1
    while max_num // exp > 0:
        count_sort_radix(arr, exp)
        exp *= 10

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", radix_sort(seq))

