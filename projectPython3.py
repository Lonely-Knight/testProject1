from functools import cmp_to_key


def comparison(a, b):
    return int(b + a) - int(a + b)


def max_number(str_list):
    sorted_numbers = sorted(str_list, key=cmp_to_key(comparison))
    return ''.join(sorted_numbers)


input_list = ["41", "4", "005", "89"]
result = max_number(input_list)
print(result)
