Gstart = int(input('Input start gauge '))
Gend = int(input('Input final gauge '))
Tm = Gstart - Gend
print('You loaded',Tm,'m3')


if (Tm > 0 and Tm <= 24 ):
        print('This is small load')
elif (Tm < 0):
	print('Start gauge cant be smaller than end gauge')
elif (Tm > 24 and Tm < 30):
	print('This is big load')
else:
	print('You are overloaded')
	



