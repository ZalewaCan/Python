Gstart = int(input('Input start gauge '))
Gend = int(input('Input final gauge '))
Tm = Gstart - Gend
print('You loaded',Tm,'m3')
b = Tm

if (b < 24 ):
        print('This is small load')
elif (b < 0):
	print('Start gauge cant be smaller than end gauge')
elif (b > 24 and b < 30):
	print('This is big load')
else:
	print('You are overloaded')
	



