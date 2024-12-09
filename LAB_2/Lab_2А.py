def is_valid(expr):
    # Проверка окончания на "=" и правильности скобок
    if not expr.endswith('='):
        return False, "Выражение должно заканчиваться знаком '='."

    stack = []
    for i, c in enumerate(expr[:-1]):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False, "Ошибка: лишняя закрывающая скобка."
            stack.pop()
        # Проверка деления на ноль
        if c == '/' and expr[i + 1] == '0':
            return False, "Ошибка: деление на ноль."

    if stack:
        return False, "Ошибка: лишняя открывающая скобка."

    return True, expr[:-1]  # убираем "=" для вычислений


def calc(expr):
    try:
        return eval(expr)
    except Exception:
        return "Ошибка в вычислении."


def main():
    expr = input("Введите арифметическое выражение (окончание '='): ")
    valid, processed_expr = is_valid(expr)

    if valid:
        result = calc(processed_expr)
        print(f"Результат: {result}")
    else:
        print(processed_expr)  # Вывод сообщения об ошибке


if __name__ == "__main__":
    main()
