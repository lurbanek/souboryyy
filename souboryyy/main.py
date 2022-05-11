import random
def menu():
    try:
        f1 = open(input('Zadej prvni soubor > '), 'r')
        f2 = open(input('Zadej druhy soubor > '), 'w')
    except FileNotFoundError:
        print('Zadal jsi spatnou slozku')
        exit(1)

    run = True
    while run:
        print('''
        1 - Prevod souboru na mala pismena
        2 - Nahrazeni vyskytu jednoho znaku jinym znakem
        3 - Statistika souboru
        4 - Generovani nahodneho textu
        ''')
        volba = input('Jakou akci chcete provest? > ')
        if volba == '1':
            prevod_pismen(f1, f2)
        elif volba == '2':
            nahrazeni(f1, f2, input('Zaden znak1 > '), input('Zadej znak 2 > '))
        elif volba == '3':
            statistika(f1)
        elif volba == '4':
            maxwords = int(input('Zadej pocet slov > '))
            while maxwords < 1:
                print('Neplatny pocet slov')
                maxwords = int(input('Zadej pocet slov > '))
            sentence_gen(maxwords, f2)
        else:
            run = False
            f1.close()
            f2.close()

def prevod_pismen(file1, file2):
    for line in file1:
        file2.write(line.lower())

def nahrazeni(file1, file2, znak1, znak2):
    while True:
        pismeno = file1.read(1)
        if pismeno == '':
            file1.seek(0)
            break
        else:
            if pismeno.upper() == znak1.upper(): #Case sensitive osetreni
                file2.write(znak2)
            else:
                file2.write(pismeno)

def statistika(file1):
    znaky = {}
    while True:
        pismeno = file1.read(1)
        if pismeno == '':
            file1.seek(0)
            break
        else:
            if pismeno not in znaky.keys():
                znaky[pismeno] = 1
            else:
                znaky[pismeno] += 1
    for key in sorted(znaky.keys()):
        if key == '\n':
            print(f'(\\n) --- {znaky[key]}')
        else:
            print(f'({key}) --- {znaky[key]}')

def word_gen(minchars = 2, maxchars = 10):
    samohlasky = 'aeiyou'
    souhlasky = 'qwrtpsdfghjklzxcvbnm'
    pocet = random.randint(minchars, maxchars)
    vysledek = ''
    zacatek = random.randint(0, 1)
    for i in range(pocet):
        if i % 2 == zacatek:
            vysledek += random.choice(samohlasky)
        else:
            vysledek += random.choice(souhlasky)
    return vysledek

def sentence_gen(maxwords, file2):
    vysledek = ''
    for i in range(maxwords):
        vysledek += word_gen() + ' '
    vysledek = vysledek.capitalize()[0:-1] + '.\n'
    for line in vysledek:
        file2.write(line)

if __name__ == "__main__":
    menu()
