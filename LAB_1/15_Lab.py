class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Прямой обход (Pre-order)
    def traversePreOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Центральный обход (In-order)
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Обратный обход (Post-order)
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=' ')


def find_right_subtree(string, start, end):
    # Счетчик открытых скобок для нахождения правого поддерева
    bracket_counter = 0
    while start < end:
        if string[start] == ',' and bracket_counter == 0:
            return start + 1  # Нашли разделитель между левым и правым поддеревом
        if string[start] == '(':
            bracket_counter += 1
        if string[start] == ')':
            bracket_counter -= 1
        start += 1
    return -1  # Если не нашли, возвращаем -1


def create_subtree(string, start, end):
    while start < end and (string[start] == ' ' or string[start] == '('):
        start += 1  # Пропускаем пробелы и открывающие скобки

    if start >= end:
        return None  # Пустое поддерево

    # Чтение значения узла
    number = ''
    while start < end and string[start].isdigit():
        number += string[start]
        start += 1

    node = Node(int(number))  # Создаем узел с числовым значением

    # Ищем точку раздела для правого поддерева
    right_subtree_index = find_right_subtree(string, start, end)

    if right_subtree_index == -1:
        raise Exception("Wrong bracket notation string!")  # Ошибка в скобочной записи

    # Рекурсивное создание левого и правого поддеревьев
    node.left = create_subtree(string, start + 1, right_subtree_index - 1)
    node.right = create_subtree(string, right_subtree_index, end - 1)

    return node


def create_tree(string):
    return create_subtree(string, 0, len(string))


# Главная программа
if __name__ == "__main__":
    # Вводим строку с линейной скобочной нотацией
    tree_str = input("Please, enter the linear-bracket string: ").strip()

    # Создаем дерево
    root = create_tree(tree_str)

    # Вызов обходов дерева
    print('Pre-Order traversal:')
    root.traversePreOrder()
    print('\n')

    print('In-Order traversal:')
    root.traverseInOrder()
    print('\n')

    print('Post-Order traversal:')
    root.traversePostOrder()
    print()
