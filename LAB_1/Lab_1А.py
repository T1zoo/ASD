def to_list(s):
    return list(s)

def check_brackets(s):
    is_valid = False
    pairs = {'(': ')', '[': ']', '{': '}'}
    i = 0

    while len(s) > 1:
        # Проверяем текущий символ на наличие открывающей скобки
        if s[i] in pairs:
            closing = pairs[s[i]]
            # Проверяем, если сразу за открывающей скобкой идет закрывающая
            if i + 1 < len(s) and s[i + 1] == closing:
                # Удаляем пару скобок и начинаем с начала
                del s[i + 1]
                del s[i]
                is_valid = True
                i = 0
                continue

            if i + 1 < len(s) and s[i - 1] == closing:
                # Удаляем пару скобок и начинаем с начала
                del s[i - 1]
                del s[i]
                is_valid = True
                i = 0
            else:
                is_valid = False
                break
        else:
            is_valid = False
            break

    if is_valid:
        print(s)
        print('Строка существует')
    else:
        print(s)
        print('Строка не существует')

# Пример ввода
str_input = '()[((())}'
str_list = to_list(str_input)
check_brackets(str_list)
