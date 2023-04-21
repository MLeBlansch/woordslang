import numpy as np

grouped = dict()
start_letters = dict()
end_letters = dict()

for letter in range(ord('A'), ord('Z') + 1):
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


# TODO: plots for order number per start/end letter and groups