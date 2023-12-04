holder = 0
concatenate = 0

with open('input_day_01.txt', 'r') as file:
    for line in file:
        numeric_string = ''.join(filter(str.isdigit, line))  # вытаскиваем только цифры
        concatenate = int(numeric_string[0] + numeric_string[-1])
        holder = holder + concatenate
print(holder)
