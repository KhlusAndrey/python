# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

operation_type = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for i in range(len(operation_type)):
    print(operation_type[i], type(operation_type[i]))
