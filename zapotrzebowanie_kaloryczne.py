#Praca siedząca, brak dodatkowej aktywności fizycznej
wysilek1 = 1.2
#Praca niefizyczna, mało aktywny tryb życia
wysilek2 = 1.4
#Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu
wysilek3 = 1.6
#Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu
wysilek4 = 1.8
#Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu
wysilek5 = 2.0
#wspolczynnik S
mezczyznaS = 5
kobietaS = -161
print('Jestes (M)ezczyzna czy (K)obieta')
wybplci = str(input())
print('Jaka jest twoja masa')
masa = int(input())
print('Jaka jest twoja wzrost')
wzrost = int(input())
print('Jaki jest twoja wiek')
wiek = int(input())
if wybplci == 'M':
    wspS = mezczyznaS
else:
    wspS = kobietaS
print('Wybierz twoj dzienny rodzaj aktywnosci fizycznej: \n(1)Praca siedząca, brak dodatkowej aktywności fizycznej \n(2)Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu \n(3)Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu \n(4)Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu \n(5)Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu')
wysilek = str(input())
if wysilek == '1':
    wysilektot = wysilek1
elif wysilek == '2':
    wysilektot = wysilek2
elif wysilek == '3':
    wysilektot = wysilek3
elif wysilek == '4':
    wysilektot = wysilek4
else:
    wysilek == '5'
    wysilektot = wysilek5

podszapot = (10 * masa + 6.25 * wzrost + 5 * wiek + wspS)
zapotkal = podszapot * wysilektot
print('Twoje zapotrzebowanie kaloryczne to:', zapotkal, 'kcal')
