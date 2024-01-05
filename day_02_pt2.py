reds_max, greens_max, blues_max = 0, 0, 0  # to place the minimum required int in each game
single_game_power = 1  # to multiply the minimum required rgb ints for each game
all_games_power = 0 #to sum up all powers

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
                print('reds = ', reds) #debug
                if reds > reds_max: #find the max of each r/g/b for a game. The max amount present will be a min amount reqired for the game to be possible
                    reds_max = reds
                    print('reds_max =', reds_max)
            elif 'green' in templine:
                greens = int(''.join(filter(str.isdigit, templine)))
                print('greens = ', greens) #debug
                if greens > greens_max:
                    greens_max = greens
                    print('greens_max =', greens_max)
            elif 'blue' in templine:
                blues = int(''.join(filter(str.isdigit, templine)))
                print('blues = ', blues) #debug
                if blues > blues_max:
                    blues_max = blues
                    print('blues_max =', blues_max)

            del line[0] #deletes element with index 0, next one becomes 0

        if len(line) == 0: #the line has iterated completely
            single_game_power = reds_max * blues_max * greens_max #we multiply the min amount of each r/g/b required to find the power of a single game
            print('single_game_power =', single_game_power)
            all_games_power += single_game_power #we sum up all the power of all single games
            print('all_games_power =', all_games_power)

            single_game_power = 0 #erase old single game power
            reds_max, greens_max, blues_max = 0, 0, 0 #erase the maxes of the previous single game

print('all games power final =', all_games_power)