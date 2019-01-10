Odostart = int (input('Odometer start '))
Odoend = int (input('Odometer end '))
Loads = int (input('Number of loads hauled '))
Totalkm = Odoend - Odostart
Kmperld = Totalkm / Loads
#Diesel cost in CAD
DieselCost = 0.89
#Diesel consumption in litres per 1 km
DieselConsumption = 0.69
print ('***********************************')
print ('You have driven', Totalkm, 'km')
print ('You averaged', Kmperld, 'km per load')
print ('Avg diesel cost per load', '$',Kmperld * DieselConsumption * DieselCost)