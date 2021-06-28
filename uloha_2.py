# 2. Text V dlouhém textu zkuste najít pro libovolná dvě slova jejich nejmenší vzdálenost na počet slov
# (např. v 'Ahoj Krabe, řekla ryba' je 'Ahoj' a 'ryba' vzdaleno 2 slova).
# Dokážete to i napsat, aby to bylo casove narocne O(1)?

text = input('Vložte svůj text: ').lower().split()
slova = input('První a poslední slovo: ').lower().split()
indexy = []
delka = []

if slova[0] and slova[1] in text:
    if slova[0] == slova[1]:
        print('Stejná slova')
    else: 
        while slova[0] in text:
            indexy.append([text.index(slova[0]), 'slovo_0'])
            text[text.index(slova[0])] = slova[0] + slova[0]
        while slova[1] in text:
            indexy.append([text.index(slova[1]), 'slovo_1'])
            text[text.index(slova[1])] = slova[1] + slova[1]
        indexy.sort()
        i = 0
        while i+1 < len(indexy):
            if indexy[i][-1] != indexy[i+1][-1]:
                delka.append(indexy[i+1][0]-indexy[i][0]-1)
                i = i + 1
else:
    print('Slova nejsou v textu!')

print(f"{slova[0]} a {slova[1]} jsou od sebe {min(delka)} slov daleko")