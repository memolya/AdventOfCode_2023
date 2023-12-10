holder = 0
concatenate = 0
#declare empty list for outer cycle
list_converted = []

with open('input_day_01.txt', 'r') as file:
        for line in file:
            for line in file:
                # words to numbers
                if 'one' in line:
                    list_converted.append(1)
                elif 'two' in line:
                    list_converted.append(2)
                elif 'three' in line:
                    list_converted.append(3)
                elif 'four' in line:
                    list_converted.append(4)
                elif 'five' in line:
                    list_converted.append(5)
                elif 'six' in line:
                    list_converted.append(6)
                elif 'seven' in line:
                    list_converted.append(7)
                elif 'eight' in line:
                    list_converted.append(8)
                elif 'nine' in line:
                    list_converted.append(9)
                # numbers as they are
                elif '1' in line:
                    list_converted.append(1)
                elif '2' in line:
                    list_converted.append(2)
                elif '3' in line:
                    list_converted.append(3)
                elif '4' in line:
                    list_converted.append(4)
                elif '5' in line:
                    list_converted.append(5)
                elif '6' in line:
                    list_converted.append(6)
                elif '7' in line:
                    list_converted.append(7)
                elif '8' in line:
                    list_converted.append(8)
                elif '9' in line:
                    list_converted.append(9)
            concatenate = int(numeric_string[0] + numeric_string[-1])
            holder = holder + concatenate
print(holder)



