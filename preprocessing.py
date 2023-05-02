import numpy as np
from plotting import plot_bars

grouped = dict()        # key: start and end letter, value: number of animals
start_letters = dict()  # key: start letter, value: number of animals
end_letters = dict()    # key: end letter, value: number of animals

for letter in range(ord('A'), ord('Z') + 1):
    letter = chr(letter)
    start_letters[letter] = 0
    end_letters[letter] = 0

with open('data/animals_no_bracket.txt', 'r', encoding='utf-8') as f:
    for animal in f.readlines():
        animal = animal.strip()

        start = str.upper(animal[0])
        end = str.upper(animal[-1])
        key = str.upper(f'{start}{end}')
        
        start_letters[start] += 1
        end_letters[end] += 1

        try:
            grouped[key] += 1
        except KeyError:
            grouped[key] = 1


parsed = list(grouped.items())
list.sort(parsed, key=lambda item: item[0])

with open('data/groups.txt', 'w', newline='\n', encoding='utf-8') as f:
    f.writelines([f'{el[0]}\t{el[1]}\n' for el in parsed])

print('Starting letters: ', sorted(list({entry[0][0] for entry in parsed})))
print('Ending letters: ', sorted(list({entry[0][-1] for entry in parsed})))
print('Total animals: ', np.sum(list(grouped.values())))

plot_bars(list(start_letters.items()), 'Starting letters', 'Letter', 'Count', True, 'starting_letters.png')
plot_bars(list(end_letters.items()), 'Ending letters', 'Letter', 'Count', True, 'ending_letters.png')
