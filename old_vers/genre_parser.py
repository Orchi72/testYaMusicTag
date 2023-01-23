import os
import shutil

print('Start!')
print('________________\n')

#with open('log/genre.txt', 'r') as f:
with open('log/TempData.txt', 'r') as f:
    Lines = f.readlines()

Genres = []
count = 0

for line in Lines:

    if line.strip() != '':
        #print(line.strip())
        count += 1

        if line.strip() not in Genres:
            Genres.append(line.strip())



print(f'Scan: {count}, origin: {len(Genres)}')

for line in Genres:
    print(line.strip())