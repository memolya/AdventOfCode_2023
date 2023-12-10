holder = 0
concatenate = 0
replaced_line = 0
new_line = 0
replacements = [('threeight', '38'), ('twone', '21'), ('fiveight', '58'), ('sevenine', '79'), ('nineight', '98'), ('eightwo', '82'), ('eighthree', '83'), ('oneight', '18'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')]

with open('input_day_01.txt', 'r') as file:
    #iterate the whole file
    for line in file:
        # replace words and mixed up words with numbers
        for char, replacement in replacements:
            if char in line:
                new_line = line.replace(char, replacement)
                line = new_line #every time a replacement is done the line is updated so the next iteration of replacement can happen
        #now all the lines consist of numbers and random letters
        print(line)


