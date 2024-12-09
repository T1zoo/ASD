#ПИРАМИДАЛЬНАЯ (HEAP SORT)

def heapify(arr, n, i):
    max_i = i  # Инициализируем корень как максимальный элемент
    l = 2 * i + 1  # Левый дочерний элемент
    r = 2 * i + 2  # Правый дочерний элемент

    # Проверяем, если левый дочерний элемент больше корня
    if l < n and arr[l] > arr[max_i]:
        max_i = l

    # Проверяем, если правый дочерний элемент больше текущего максимума
    if r < n and arr[r] > arr[max_i]:
        max_i = r

    # Если максимальный элемент не корень, меняем их местами и продолжаем heapify
    if max_i != i:
        arr[i], arr[max_i] = arr[max_i], arr[i]
        heapify(arr, n, max_i)

def heap_sort(arr):
    n = len(arr)

    # Построение max-кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        arr[i], arr[0] = arr[0], arr[i]
        # Применяем heapify к уменьшенной куче
        heapify(arr, i, 0)

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", heap_sort(seq))

