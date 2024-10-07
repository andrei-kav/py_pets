import random
import time

# random number from 1 till 10
# print(random.randint(1, 10))

team1_name = 'Milan'
team1_rank = 3

team2_name = 'Juve'
team2_rank = 12

team1_chance = 16 - team1_rank
team2_chance = 16 - team2_rank

team1_chance += random.randint(0, 16)
team2_chance += random.randint(0, 16)

print('The pickalator is now choosing a winner...\n')
time.sleep(2)

print('...almost there...\n')
time.sleep(2)

# max possible rank is 15+16=31
max_rank = 31

if team1_chance > team2_chance:
    confidence = (team1_chance - team2_chance) / max_rank * 100
    print(f'The pickalator has chosen: {team1_name} with {int(confidence)}% confidence ')
else:
    confidence = (team2_chance - team1_chance) / max_rank * 100
    print(f'The pickalator has chosen: {team2_name} with {int(confidence)}% confidence ')

print(f'team 1 {team1_name}, {team1_chance}')
print(f'team 2 {team2_name}, {team2_chance}')