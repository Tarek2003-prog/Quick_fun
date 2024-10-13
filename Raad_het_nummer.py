import random
Gebruikers_naam = str(input('Wat is je naam? '))
print (f'Beste {Gebruikers_naam} in dit spel moet je het getal raden. Het maximum getal mag je zelf kiezen. De aantal pogingen mag je ook zelf kiezen.')
print ('Succes :)')
max_getal = int(input(f'{Gebruikers_naam} kies het maximum getal waaruit geraden moet worden: '))
pogingen = int(input('In hoeveel keer wil je raden?: '))
willekeurige_getal = random.randint(1, max_getal)
#De gebruiker krijgt de mogelijkheid om zelf de max getal te kiezen.
print (f'Raad een getal tussen 1 en {max_getal} ')
#De gebruiker keist zelf in hoeveel pogingen hij gaat raden.
print (f'Je hebt {pogingen} pogingen om het juiste getal te raden ')

for poging in range(1, pogingen + 1):
    gok =  int(input(f'Poging {poging} van {pogingen} wat is je gok? '))

    if gok == willekeurige_getal:
        print(f'{Gebruikers_naam} Gefeliciteerd! Je hebt het juiste getal {willekeurige_getal} geraden in {poging} pogingen ')
        break
    elif gok < willekeurige_getal:
        print('Het getal is hoger. ')
    else:
        print ('Het getal is lager ')

    if poging == pogingen:
        print (f'Je hebt helaas geen pogingen meer, het juiste getal is {willekeurige_getal}' )
