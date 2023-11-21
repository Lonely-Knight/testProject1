from functools import cmp_to_key

# функция сравнения рядом находящихся чисел
def comparison(a, b):
    return int(b + a) - int(a + b)

# функция сортировки и объединения отсортированного массива входных данных в наибольшее число
def max_number(str_list):
    sorted_numbers = sorted(str_list, key=cmp_to_key(comparison))
    return ''.join(sorted_numbers)


input_list = ["41", "4", "005", "89"]
result = max_number(input_list)
print(result)
