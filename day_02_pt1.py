id_holder = 0 #game id
red_max = 12 #reds max
green_max = 13 #greens max
blue_max = 14 #blues max
reds, greens, blues = 0, 0, 0 #to cut out integers for each color in line

with open('input_day_02.txt', 'r') as file:
    #iterate the whole file
    for line in file:
        # replace ';' with ',' so we can split by ','
        # replace ':' with ',' so we can delete 'Game n'
        line = line.replace(':', ',')
        line = line.replace(';', ',')
        line = line.split(',') #split the lines by comma
        print(line) #debug
        game_id = line[0] #before removing game id for correct [0] element next cycle iteration we store it here
        game_id = int(''.join(filter(str.isdigit, game_id))) #taking only numbers from game id
        print(game_id) #debug
        del line[0]
        while len(line) > 0: #cycle in the lenghth of the single line
            templine = line[0]
            print(templine) #debug

            if 'red' in templine:
                reds = int(''.join(filter(str.isdigit, templine)))
                if reds > red_max:
                    break
                print('reds = ', reds) #debug
            elif 'green' in templine:
                greens = int(''.join(filter(str.isdigit, templine)))
                if greens > green_max:
                    break
                print('greens = ', greens) #debug
            elif 'blue' in templine:
                blues = int(''.join(filter(str.isdigit, templine)))
                if blues > blue_max:
                    break
                print('blues = ', blues) #debug

            del line[0] #deletes element with index 0, next one becomes 0
            if len(line) == 0: #only possible when break didn't occur in whole line cycle (so all the numbers do not exceed max)
                id_holder += game_id

                print('id_holder = ', id_holder)
