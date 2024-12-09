#ВСТАВКАМИ

def ins_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1

        # Сдвигаем элементы arr[0...i-1], которые больше val, на одну позицию вправо
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем val на его правильное место
        arr[j + 1] = val

    return arr

# Пример использования
seq = list(map(int, input("Введите числа через пробел: ").split()))
print("Отсортированная последовательность:", ins_sort(seq))

